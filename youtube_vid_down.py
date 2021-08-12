from pytube import YouTube


def main():
    url = input("Enter video url: ")
    video = YouTube(url)
    download_dir = input("Enter directory to save video in:> ")
    video.streams.order_by('resolution').desc().first().download(download_dir)

if __name__ == '__main__':
    while True:
        try:
            action = input("Enter 1 to download video or otherwise to quit:> ")
            if int(action) == 1:
                main()
            else:
                break
        except ValueError:
            print("Use a number instead...")
