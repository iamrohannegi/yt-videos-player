import PySimpleGUI as sg 
from playlist import play_videos
import multiprocessing 
from queue import Queue 

songs = []

frame = [
    [sg.T("Video Title")],
    [sg.T("Video Length"), sg.T("(3/24)")],
]

tab_1 = [
    [sg.Frame("Currently playing", frame)],
    [sg.B("Play")]
]

table_heading = ["Video Name"]

tab_2_col_1 = [
    [sg.Table(headings=table_heading, values=songs, key="-TABLE-")],
]

tab_2_col_2_frame = [
    [sg.T("Enter video Title")],
    [sg.I(key="-VIDNAME-")],
    [sg.B("Add")]
]

tab_2_col_2 = [
    [sg.Frame("Add a video", tab_2_col_2_frame)],
]

tab_2 = [
    [sg.Col(tab_2_col_1), sg.VerticalSeparator(), sg.Col(tab_2_col_2)]
]


layout = [
    [sg.TabGroup([
        [sg.Tab("Main", tab_1), sg.Tab("Edit", tab_2)]
    ])],
    [sg.Exit()],
] 

window = sg.Window("Playlist", layout)


if __name__ == '__main__':
    proc = None
    while True:
        event, values = window.read()
        print(event, values)

        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event == "Play":
            proc = multiprocessing.Process(target=play_videos, args=([song[0] for song in songs], ))
            proc.start()
        elif event == "Add" and values["-VIDNAME-"]:
            songs.append([values["-VIDNAME-"]])
            print(songs)
            window["-TABLE-"].update(values=songs)

        print(songs)

    if proc and proc.is_alive():
        proc.terminate()
    window.close()