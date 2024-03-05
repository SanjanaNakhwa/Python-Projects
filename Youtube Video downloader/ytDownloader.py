# Import necessary modules
from pytube import YouTube
from sys import argv

# Extract the YouTube video URL from command line arguments
link = argv[1]

# Create a YouTube object for the provided video URL
yt = YouTube(link)

# Print the title and views count of the video
print("Title : ", yt.title)
print("View ", yt.views)

# Get the highest resolution stream available for the video
yd = yt.streams.get_highest_resolution()

# Check if a stream with the highest resolution is available
if yd:
    try:
        # Download the video to the specified directory
        yd.download('/Users/sanjananakhwa/Downloads/Youtube Videos')
        print("Video Downloaded successfully!")
    except Exception as e:
        # Handle any errors that occur during the download process
        print("Error occurred while downloading:", e)
else:
    # If no stream with the highest resolution is available
    print("No stream available for the highest resolution.")
