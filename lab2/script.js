let xhr = new XMLHttpRequest();
xhr.open("GET", "reminders.xml", true);
xhr.send();

xhr.onload = function () {
    if (xhr.status == 200) {
        let xmlDoc = xhr.responseXML;
        let reminders = xmlDoc.getElementsByTagName("reminder");

        let output = document.querySelector('.reminders');
        output.innerHTML = "";

        for (let i = 0; i < reminders.length; i++) {
            console.log(i)
            let reminderItem = getReminder(i, reminders);
            output.appendChild(reminderItem);
        }

        let input = document.querySelector(".num");
        if (input) {
            input.onchange = function () {
                let index = Number(input.value)
                if (index || index === 0) {
                    let numOutput = document.querySelector('.num-output');
                    numOutput.innerHTML = '';
                    let reminderItem = getReminder(index, reminders);
                    numOutput.appendChild(reminderItem);
                }
            }
        }

    } else {
        console.log("unable to open xml");
    }

}

function getReminder(index, reminders) {
    let reminder = reminders[index]
    let title = reminder.getElementsByTagName("title")[0].textContent;
    let date = reminder.getElementsByTagName("date")[0].textContent;

    const reminderItem = document.createElement('div');
    reminderItem.className = "reminder-item";
    reminderItem.innerHTML = `
    <div class="reminder-body">
        <input type="checkbox" name="" id="">
        <a class="reminder-title" href="#">${title}</div>
    </div>
    <div class="reminder-footer">${date}</div>`

    return reminderItem;
}