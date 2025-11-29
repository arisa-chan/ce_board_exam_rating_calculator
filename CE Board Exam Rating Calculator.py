#
# CE BOARD EXAM RATING CALCULATOR
# A simple application to calculate your rating in civil engineering
# licensure examination based on your scores.
#
# version 1.0 by Engr. Jaydee N. Lucero
#
# Python version: 3.14
# GUI framework: FreeSimpleGUIQt 5.2.0
#
import FreeSimpleGUIQt as sg
sg.theme("Material2")

layout_mst = [
    [sg.Text("MSTC", justification='l', font=("Tahoma", 10, "bold"))],
    [sg.Input(key="-SCORE_MSTC-", size=(8,2), justification='c', font=("Tahoma", 32)), sg.Text("/75")],
    [sg.Text("", key="-RATING_MSTC-", justification='c')]
]

layout_hge = [
    [sg.Text("HGE", justification='l', font=("Tahoma", 10, "bold"))],
    [sg.Input(key="-SCORE_HGE-", size=(8,2), justification='c', font=("Tahoma", 32)), sg.Text("/50")],
    [sg.Text("", key="-RATING_HGE-", justification='c')]
]

layout_psad = [
    [sg.Text("PSAD", justification='l', font=("Tahoma", 10, "bold"))],
    [sg.Input(key="-SCORE_PSAD-", size=(8,2), justification='c', font=("Tahoma", 32)), sg.Text("/75")],
    [sg.Text("", key="-RATING_PSAD-", justification='c')]
]

layout_menu = [
    ["Home", ["About", "Exit"]]
]

layout = [
    [sg.Menu(layout_menu, background_color="lightblue")],
    [sg.Column(layout_mst), sg.Column(layout_hge), sg.Column(layout_psad)],
    [sg.Button("Calculate"), sg.Stretch(), sg.Text("", key="-RATING-"), sg.Text("", key="-PASSED-")]
]

window = sg.Window("CE Board Exam Rating Calculator", layout)

while True :
    event, values = window.read()

    if event is None or event == "Exit" or event == sg.WIN_CLOSED :
        break
    elif event == "Calculate" :
        try :
            score_mstc = int(values["-SCORE_MSTC-"])
            score_hge = int(values["-SCORE_HGE-"])
            score_psad = int(values["-SCORE_PSAD-"])

            if (score_mstc < 0 or score_mstc > 75 or score_hge < 0 or score_hge > 50 or score_psad < 0
                    or score_psad > 75) :
                raise ValueError
        except ValueError :
            sg.popup(
                "Inputted values outside bounds\n"
                "\n"
                "0 ≤ score in MSTC ≤ 75\n"
                "0 ≤ score in HGE ≤ 50\n"
                "0 ≤ score in PSAD ≤ 75"
            , title="Error")
            continue

        rating_mstc = score_mstc/75*100
        rating_hge = score_hge/50*100
        rating_psad = score_psad/75*100

        if rating_mstc < 50 :   window["-RATING_MSTC-"].update("{0:.2f}%".format(rating_mstc), background_color="red",
                                                               text_color="white")
        else :                  window["-RATING_MSTC-"].update("{0:.2f}%".format(rating_mstc), background_color="green",
                                                               text_color="white")

        if rating_hge < 50 :    window["-RATING_HGE-"].update("{0:.2f}%".format(rating_hge), background_color="red",
                                                              text_color="white")
        else :                  window["-RATING_HGE-"].update("{0:.2f}%".format(rating_hge), background_color="green",
                                                              text_color="white")

        if rating_psad < 50 :   window["-RATING_PSAD-"].update("{0:.2f}%".format(rating_psad), background_color="red",
                                                               text_color="white")
        else :                  window["-RATING_PSAD-"].update("{0:.2f}%".format(rating_psad), background_color="green",
                                                               text_color="white")

        rating = 0.35*rating_mstc + 0.30*rating_hge + 0.35*rating_psad
        window["-RATING-"].update("Rating: {0:.2f}%".format(rating))

        if rating_mstc < 50 or rating_hge < 50 or rating_psad < 50 or rating < 70 :
            window["-PASSED-"].update("FAILED", background_color="red", text_color="white", font=("Tahoma", 10,
                                                                                                  "bold"))
        else :
            window["-PASSED-"].update("PASSED", background_color="green", text_color="white", font=("Tahoma", 10,
                                                                                                    "bold"))
    elif event == "About" :
        sg.popup(
            "CE Board Exam Rating Calculator\n"
            "version 1.0\n"
            "(c) 2025 by Engr. Jaydee N. Lucero\n"
            "\n"
            "Python version: 3.14\n"
            "GUI framework: FreeSimpleGUI 5.2.0"
        , title="About")

window.close()