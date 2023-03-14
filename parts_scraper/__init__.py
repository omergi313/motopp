import pandas as pd
from parts_scraper.sources import RevZillaSource
from parts_scraper.part import PartsScraper


def run() -> pd.DataFrame:
    revzilla1 = PartsScraper(
        "https://www.revzilla.com/sportbike-parts", RevZillaSource()
    )
    revzilla2 = PartsScraper(
        "https://www.revzilla.com/sportbike-parts?view_all=&page=2", RevZillaSource()
    )
    df = pd.concat([revzilla1.df, revzilla2.df])

    return df


if __name__ == '__main__':
    run()
