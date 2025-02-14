let xhr = new XMLHttpRequest();
xhr.open("GET", "reminders.xml", true);
xhr.send();

xhr.onload = function () {
    if (xhr.status == 200) {
        let xmlDoc = xhr.responseXML;
        let reminders = xmlDoc.getElementsByTagName("reminder");

        let output = document.querySelector('.reminders');
        output.innerHTML = "";
        
        for (let reminder of reminders) {
            let title = reminder.getElementsByTagName("title")[0].textContent;
            let date = reminder.getElementsByTagName("date")[0].textContent;

            const reminderItem = document.createElement('div');
            reminderItem.className = "reminder-item";
            reminderItem.innerHTML = `
            <div class="reminder-body">
                <input type="checkbox" name="" id="">
                <div class="reminder-title">${title}</div>
            </div>
            <div class="reminder-footer">${date}</div>`

            output.appendChild(reminderItem);
        }
    } else {
        console.log("Ошибка при открытии XML");
    }
}