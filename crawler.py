from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as soup
import os



def get_html(url):

    playwright = sync_playwright().start()
    browser = playwright.webkit.launch(headless=True)

    page = browser.new_page()
    page.goto(url)

    for _ in range(50):
        page.mouse.wheel(0, 7000)
        page.wait_for_timeout(500)

    html = page.content()
    
    browser.close()
    playwright.stop()

    return html



def crawl_html(html):

    html = soup(html, 'html.parser')

    attributes = {
        "id": "text",
        "class": "style-scope ytd-thumbnail-overlay-time-status-renderer"
    }

    video_time_tags = html.find_all('span', attributes)
    video_times = []

    for i in range(0, len(video_time_tags), 2):

        raw_time = video_time_tags[i].get_text()
        
        stripped_time = raw_time.split()
        final_time = str().join(stripped_time) + '\n'

        video_times.append(final_time)

    video_times = str().join(video_times)


    if not os.path.isfile('video_times.txt'):
        open('video_times.txt', 'w').write('')
    
    file = open('video_times.txt', 'r').read()
    file += '\n' + video_times

    open('video_times.txt', 'w').write(file)



def count_video_times():

    timesSum = [0, 0, 0] 

    file = open('video_times.txt', 'r').read()
    sliced_times = file.split('\n') # split the file lines

    #split every h:m:s into [h, m, s]
    sliced_times = [sliced_times[i].split(':') for i in range(len(sliced_times))] 
    
    # deleting empty spaces on first and last indexes
    del sliced_times[0]
    del sliced_times[-1]

    # summing every unit regularly because every time var may be [sec], [min, sec] and [hour, min, sec]
    videos = 0
    for time in sliced_times:
        units = len(time)

        # ignoring empty spaces
        if time != ['']:
            videos += 1
            match units:
                case 1:
                    timesSum[2] += int(time[0])
                case 2:
                    timesSum[1] += int(time[0])
                    timesSum[2] += int(time[1])
                case 3:
                    timesSum[0] += int(time[0])
                    timesSum[1] += int(time[1])
                    timesSum[2] += int(time[2])
        
    units = [24, 60, 60]
    final_sum = [0, 0, 0, 0]

    for i in range(2, -1, -1):
        mid_sum = timesSum[i]+final_sum[i+1]
        final_sum[i+1] = mid_sum % units[i]
        final_sum[i] = mid_sum // units[i] 

    average = 0 
    average += final_sum[3]
    average += final_sum[2]*60
    average += final_sum[1]*60*60
    average += final_sum[0]*24*60*60
    average = average//videos
    average = [average//60, average%60]

    final_sum.append(average)
    return final_sum
                


def main(id):

    print('\n   [Crawling Youtube...]\n')
    open('video_times.txt', 'w').write('') #restarting static file

    urls = [
        f'https://www.youtube.com/@{id}/videos',
        f'https://www.youtube.com/@{id}/streams'
    ]

    for url in urls:
        html = get_html(url)
        crawl_html(html)
    
    final_time = count_video_times()
    print(f'The channel @{id} has in total\n > {final_time[0]} Days\n > {final_time[1]} Hours\n > {final_time[2]} Minutes\n > {final_time[3]} Seconds\nof video time on Youtube\n > Average video time: {final_time[4][0]} Minutes and {final_time[4][1]} seconds')



if __name__ == "__main__":

    main(input('\nType the user ID (without @): '))