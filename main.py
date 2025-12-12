from pyscript import document, display

def calculate_grade(e=None): 
    grade1 = float(document.getElementById("grade1").value)
    grade2 = float(document.getElementById("grade2").value)
    grade3 = float(document.getElementById("grade3").value)
    grade4 = float(document.getElementById("grade4").value)
    grade5 = float(document.getElementById("grade5").value)
    grade6 = float(document.getElementById("grade6").value)
    #get input value and assign to variables

    avg = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6) / 6
    #variables used to get final output

    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value
    full_Name = fname + " " + lname

    # output with HTML support
    document.getElementById("output").innerHTML = (
        f"Science: {grade1}<br>"
        f"English: {grade2}<br>"
        f"ICT: {grade3}<br>"
        f"Math: {grade4}<br>"
        f"Filipino: {grade5}<br>"
        f"PE: {grade6}"
    )

    document.getElementById("full_Name").innerHTML = f"For: {full_Name}"

    document.getElementById("final_grade").innerHTML = (
        f"Your General Weighted Average is: <strong>{avg:.2f}</strong>"
    )

club_data = {
    "Robotics": {
        "Description": "A club focused on building, programming, and competing with robots.",
        "Time": "Every Tuesday, 3:00 PM - 4:30 PM",
        "Location": "Tech Lab 2",
        "Handler": "Mr. Krabalot",
        "Category": "Academic",
        "Notes": "Join competitions and hands-on robotics training." 
    }, #assigning details into dictionaries for simplicity
    "Science": {
        "Description": "Exploring biology, chemistry, physics, and scientific experiments.",
        "Time": "Every Thursday, 3:00 PM - 4:30 PM",
        "Location": "Science Lab 1, 2, Physics Lab",
        "Handler": "Ms. Matapang",
        "Category": "Academic",
        "Notes": "Science fairs, experiments, and academic contests."
    },
    "Communication Arts": {
        "Description": "Develops skills in writing, speaking, journalism, and media.",
        "Time": "Every Monday, 3:00 PM - 4:30 PM",
        "Location": "Room 304",
        "Handler": "Mrs. Raur",
        "Category": "Academic",
        "Notes": "School paper, broadcasting, and creative writing."
    },
    "Dance Club": {
        "Description": "Focuses on modern, cultural, and performance dance.",
        "Time": "Every Friday, 3:00 PM - 5:00 PM",
        "Location": "Gymnasium, Dance Club Room",
        "Handler": "Coach Taro",
        "Category": "Non-Academic",
        "Notes": "Performances for school events and competitions."
    }
}

def show_club_info(event=None):
    selected = document.querySelector("#clubs").value
    info_box = document.querySelector("#club-info") #even=None got from ChatGPT, without it there was a consistent error message, though it functioned perfectly

    data = club_data[selected]

    html_output = f"""
        <strong>Description:</strong> {data['Description']}<br>
        <strong>Time:</strong> {data['Time']}<br>
        <strong>Location:</strong> {data['Location']}<br>
        <strong>Handler:</strong> {data['Handler']}<br>
        <strong>Category:</strong> {data['Category']}<br>
        <strong>Notes:</strong> {data['Notes']}
    """

    info_box.innerHTML = html_output





    




