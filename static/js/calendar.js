const date = new Date();

const renderCalendar = () => {
  date.setDate(1);

  const daysOfMonth = document.querySelector(".days");
  const daysOfWeek = 7;

  const lastDay = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDate();

  const prevLastDay = new Date(
    date.getFullYear(),
    date.getMonth(),
    0
  ).getDate();

  const firstDayIndex = date.getDay();

  const lastDayIndex = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDay();

  const nextDays = daysOfWeek - lastDayIndex - 1;

  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  document.querySelector(".date h1").innerHTML = months[date.getMonth()];

  document.querySelector(".date p").innerHTML = new Date().toDateString();

  let days = "";

  for (let eachPrevDay = firstDayIndex; eachPrevDay > 0; eachPrevDay--) {
    days += `<div class="prev-date">${prevLastDay - eachPrevDay + 1}</div>`;
  }

  for (let eachDay = 1; eachDay <= lastDay; eachDay++) {
    if (
      eachDay === new Date().getDate() &&
      date.getMonth() === new Date().getMonth()
    ) {
      days += `<div class="today">${eachDay}</div>`;
    } else {
      days += `<div>${eachDay}</div>`;
    }
  }

  for (let eachNextDay = 1; eachNextDay <= nextDays; eachNextDay++) {
    days += `<div class="next-date">${eachNextDay}</div>`;
    daysOfMonth.innerHTML = days;
  }
};

document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
});

document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

renderCalendar();