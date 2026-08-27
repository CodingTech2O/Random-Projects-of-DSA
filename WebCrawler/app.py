    from bs4 import BeautifulSoup
    import requests as req
    from concurrent.futures import ThreadPoolExecutor
    import os
    import time

    url = input("Enter the URL to crawl: ")
    folder_name = url.split("https://")[1].split(".")[0]

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    time.sleep(1)

    html = req.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    urls = soup.find_all("a")
    links = []

    with open(f"{folder_name}/{folder_name}.html", "a", encoding="utf-8") as file:
        file.write(soup.prettify() + "\n")

    for u in urls:
        href = u.get("href")
        if not href or href.startswith("#") or href.startswith("javascript:"):
            continue
        
        # Strip anchor fragments (e.g., convert /page#section to /page)
        href = href.split("#")[0]
        if not href:
            continue

        if href.startswith("http"):
            if href not in links:
                links.append(href)
        else:
            full_path = url.rstrip("/") + "/" + href.lstrip("/")
            if full_path not in links:
                links.append(full_path)

    print(links)
    x = 0

    def crawl(l):
        try:
            html = req.get(l, timeout=10).text
            soup = BeautifulSoup(html, "html.parser")
            
            # FIX: Clean illegal Windows characters (? : * < > | \) from filename
            raw_filename = l.split('/')[-1].split('?')[0].strip()
            if not raw_filename:
                raw_filename = f"page_{int(time.time() * 1000)}"
                
            filename = "".join(c for c in raw_filename if c not in '<>:"/\\|?*')

            urls = soup.find_all("a")
            for u in urls:
                href = u.get("href")
                if not href or href.startswith("javascript:"):
                    continue
                    
                href = href.split("#")[0]  # Strip anchor fragments
                if not href:
                    continue

                if href.startswith("http"):
                    if href not in links:
                        links.append(href)
                        with open(f"{folder_name}/links.txt", "a", encoding="utf-8") as file:
                            file.write(href + "\n")
                        if os.path.exists(f"{folder_name}/{filename}.html"):
                            filename = filename + f"_{int(time.time() * 1000)}"
                        with open(f"{folder_name}/{filename}.html", "a", encoding="utf-8") as file:
                            file.write(soup.prettify() + "\n")
                else:
                    full_path = url.rstrip("/") + "/" + href.lstrip("/")
                    if full_path not in links:
                        links.append(full_path)
                        with open(f"{folder_name}/links.txt", "a", encoding="utf-8") as file:
                            file.write(full_path + "\n")
                        if os.path.exists(f"{folder_name}/{filename}.html"):
                            filename = filename + f"_{int(time.time() * 1000)}"
                        with open(f"{folder_name}/{filename}.html", "a", encoding="utf-8") as file:
                            file.write(soup.prettify() + "\n")
        except Exception as e:
            print(f"Skipping link {l} due to request/file error: {e}")

    with ThreadPoolExecutor(max_workers=10) as executor:
        while x < len(links):
            l = links[x]
            x += 1
            print(f"Processing link {x}/{len(links)}: {l}")
            executor.submit(crawl, l)

    for l in links:
        print(l)

    print(f"Total links found: {len(links)}")
