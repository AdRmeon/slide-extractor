# slide-extractor

An easy tool to extract slides from your video lectures and presentations. 😉

## Installation

1.  Clone the repository or download the source code.
2.  Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The tool can be run directly from the command line by specifying either a local file path or a YouTube URL.

**For a local video file:**
```bash
python -m slide_extractor --path /path/to/video.mp4
```
**For a YouTube video:**
```bash
python -m slide_extractor --url "https://www.youtube.com/watch?v=..."
```

### Command-Line Options

| Short | Long        | Description                                                                                                                              | Default   |
| :---- | :---------- | :--------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| `-p`  | `--path`    | Provides the path for the video file. Use either this or `--url`.                                                                        | `None`    |
| `-u`  | `--url`     | The URL of the YouTube video you want to extract slides from. If both `-p` and `-u` are given, the local path (`-p`) will be used.         | `None`    |
| `-s`  | `--skip`    | The number of seconds to skip forward for each frame check.                                                                              | `1`       |
| `-d`  | `--diff`    | The threshold of difference required to capture a new slide. A slide is saved only if the change is greater than this value.               | `0.008`   |
| `-c`  | `--coor`    | Specifies the coordinates of a rectangular region to monitor for changes. See the detailed explanation below.                            | Full Frame |
| `-h`  | `--help`    | Shows the help menu and exits.                                                                                                           | N/A       |


### Advanced: Specifying Coordinates (`-c`, `--coor`)

This feature is incredibly useful when the video frame contains more than just the slide, such as a speaker, a banner, or other dynamic elements. By defining a "Region of Interest" (ROI), you can tell the extractor to only look for changes *within that specific area*, ignoring everything else.

To pass the coordinates, use the format `-c '[[x1,y1],[x2,y2]]'`, where `(x1, y1)` are the coordinates of the top-left corner and `(x2, y2)` are for the bottom-right corner.

**Note:** When you run the script with this option for the first time, it will show you a preview of the selected region on the first frame and pause, allowing you to verify that your coordinates are correct.

```
(0,0)
-------------------------------------------
|                                         | 
|    (x1, y1)                             |
|      ------------------------           |
|      |                      |           |
|      |                      |           | 
|      |         ROI          |           |  
|      |                      |           |   
|      |                      |           |   
|      |                      |           |       
|      ------------------------           |   
|                           (x2, y2)      |    
|                                         |             
|                                         |             
|                                         |             
-------------------------------------------(frame width, frame height)
```

## Examples

#### 1. Basic Extraction from a Local File
This will process a local video file with default settings (checking every second, difference threshold of 0.008).

```bash
python -m slide_extractor -p "lectures/computer_science_101.mp4"```
```
#### 2. Basic Extraction from YouTube
This will download and process a YouTube video with default settings.

```bash
python -m slide_extractor -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

#### 3. Advanced Extraction with Custom Parameters
This is a more complex example demonstrating the power of custom options.

```bash
python -m slide_extractor -p "/path/to/lectures/Medical_Imaging_Lecture.mkv" -s 240 -d 0.01 -c '[[300,300],[900,1700]]'
```
In this command:
*   `-p "/path/to/..."`: Specifies the video file to process.
*   `-s 240`: Jumps forward 4 minutes (240 seconds) between each frame check. This is useful for very long lectures where slides don't change often.
*   `-d 0.01`: Sets a slightly higher difference threshold, meaning it will only capture a new slide if the change is more significant.
*   `-c '[[300,300],[900,1700]]'`: Tells the script to only monitor the rectangular area defined by the top-left corner `(300,300)` and the bottom-right corner `(900,1700)` for changes.

## Tips for Better Results

Try adjusting the `diff` value if you think all slides aren't being captured or, conversely, if too many similar slides are being captured.

*   A **very low** `diff` value (e.g., `0.001`) will make the extractor capture slides even with a slight difference, like a mouse cursor appearing.
*   A **higher** `diff` value (e.g., `0.02`) might cause the extractor to miss slides with minor changes (like a single line of text being added).