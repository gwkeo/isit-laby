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
            let reminderItem = getReminder(i, reminders);
            output.appendChild(reminderItem);
        }

        let input = document.querySelector(".num");
        if (input) {
            input.onchange = function () {
                let index = Number(input.value)
                if (index || index == 0) {
                    let numOutput = document.querySelector('.num-output');
                    numOutput.innerHTML = '';
                    let reminderItem = getReminder(index, reminders);
                    numOutput.appendChild(reminderItem);
                }
            }
        }

        output.addEventListener("click", function(event) {
            let link = event.target.closest(".reminder-title");
            if (link) {
                event.preventDefault(); // Отменяем стандартный переход по ссылке
                let checkboxId = link.getAttribute("id"); // Получаем ID чекбокса
                let checkbox = document.getElementById(checkboxId);
                if (checkbox) {
                    checkbox.checked = !checkbox.checked; // Переключаем состояние
                }
            }
        })

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
    <div class="reminder">
        <input type="checkbox" id="${index}">
        <a class="reminder-title" href="#" id="${index}">${title}</div>
    </div>
    <div class="reminder-footer">${date}</div>`

    return reminderItem;
}