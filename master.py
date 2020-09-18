import emag
import evomag
import pcgarage
import time

if __name__ == '__main__':
    while(True):
        pcgarage.crawl_pcgarage()
        evomag.crawl_evomag()
        emag.crawl_emag()

        time.sleep(30)