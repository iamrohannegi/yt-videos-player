import PySimpleGUI as sg 


songs = ["Sample1", "Sample2"]

frame = [
    [sg.T("Video Title")],
    [sg.T("Video Length"), sg.T("(3/24)")],
]

tab_1 = [
    [sg.Frame("Currently playing", frame)],
]

table_heading = ["Video Name"]

tab_2_col_1 = [
    [sg.Table(headings=table_heading, values=songs)],
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

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break
    
    print(event, values)

window.close()