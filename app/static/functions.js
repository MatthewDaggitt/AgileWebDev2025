function validateStudents() {
    var groupMembers = document.getElementById('groupMembers').value;
    var student1 = document.getElementById('student1').value;
    var student2 = document.getElementById('student2').value;
    var student3 = document.getElementById('student3').value;
    var student4 = document.getElementById('student4').value;
    var email = document.getElementById('email').value;

    if (groupMembers < 1 || groupMembers > 8) {
    alert("Number of group members must be between 1 and 6.");
    return false;
    }

    if (groupMembers >= 1 && student1 === "") {
    alert("Student 1 ID is required.");
    return false;
    }
    if (groupMembers >= 2 && student2 === "") {
    alert("Student 2 ID is required.");
    return false;
    }
    if (groupMembers >= 3 && student3 === "") {
    alert("Student 3 ID is required.");
    return false;
    }
    if (groupMembers == 4 && student4 === "") {
    alert("Student 4 ID is required.");
    return false;
    }

    var studentIDs = [student1, student2, student3, student4].filter(Boolean);
    var uniqueIDs = new Set(studentIDs);
    if (uniqueIDs.size !== studentIDs.length) {
    alert("Student IDs must be unique.");
    return false;
    }

    if (!validateEmail(email)) {
    alert("Please enter a valid email address.");
    return false;
    }

    return true;
}

function validateEmail(email) {
    var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}


