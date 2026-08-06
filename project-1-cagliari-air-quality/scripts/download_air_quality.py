from pathlib import Path

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

urls = [
    "https://portal.sardegnasira.it/dettaglio-aria1?idOst=8246632&denominazione=CENCA1&rowIndex=0",
    "https://portal.sardegnasira.it/dettaglio-aria1?idOst=8246615&denominazione=CENMO1&rowIndex=1",
    "https://portal.sardegnasira.it/dettaglio-aria1?idOst=8246654&denominazione=CENQU1&rowIndex=2",
]

stations = ["CENCA1", "CENMO1", "CENQU1"]

year_selector = "select[id='_DettaglioAria_WAR_RegioneSardegnaportlet_:formReportGiornaliero:yearCombo_input']"
year_values = ["2021", "2022", "2023", "2024", "2025", "2026"]

param_selector = "select[id='_DettaglioAria_WAR_RegioneSardegnaportlet_:formReportGiornaliero:parameterCombo_input']"
param_values = [
    "Monossido di carbonio",
    "NO2",
    "Ozono",
    "PM10",
    "SO2",
    "PM2.5",
    "BENZENE",
]

results_table_selector = "div[id='_DettaglioAria_WAR_RegioneSardegnaportlet_:formReportGiornaliero:tblRilevamentiGiornalieri']"
daily_report_generator_selector = "button[id='_DettaglioAria_WAR_RegioneSardegnaportlet_:formReportGiornaliero:rilevamentoGiornaliero']"
csv_download_selector = (
    "a[id='_DettaglioAria_WAR_RegioneSardegnaportlet_:formReportGiornaliero:csvGG']"
)

loading_overlay_selector = "div[id='_DettaglioAria_WAR_RegioneSardegnaportlet_:formReportGiornaliero:j_idt231_modal']"

base = Path(__file__).parent.parent
output_directory = base / "data" / "raw" / "air_quality"

Path(output_directory).mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    year_locator = page.locator(year_selector)
    param_locator = page.locator(param_selector)
    generate_button_locator = page.locator(daily_report_generator_selector)
    results_table_locator = page.locator(results_table_selector)
    loading_overlay_locator = page.locator(loading_overlay_selector)
    csv_link_locator = page.locator(csv_download_selector)

    for url, station in zip(urls, stations):
        print(f"Processing station {station}: {url}")

        page.goto(url)
        for year in year_values:
            year_locator.select_option(year)
            for param in param_values:
                try:
                    if Path(
                        f"{output_directory}/{station}_{year}_{param.replace(' ', '_')}.csv"
                    ).exists():
                        print(
                            f"File for station {station}, year {year}, parameter {param} already exists. Skipping download."
                        )
                        continue
                    param_locator.select_option(param)
                    generate_button_locator.click()

                    results_table_locator.wait_for(timeout=90000)
                    loading_overlay_locator.wait_for(state="hidden", timeout=90000)

                    with page.expect_download() as download_info:
                        csv_link_locator.click()
                    download = download_info.value
                    download.save_as(
                        f"{output_directory}/{station}_{year}_{param.replace(' ', '_')}.csv"
                    )
                except PlaywrightTimeoutError:
                    print(
                        f"TimeoutError: Were not able to download data for station {station}, year {year}, parameter {param}."
                    )

    browser.close()
