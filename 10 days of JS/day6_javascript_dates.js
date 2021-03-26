function getDayName(dateString) {
    let date = new Date(dateString)
    const dayN = date.getDay();
    switch(dayN) {
        case 0: return "Sunday";
        case 1: return "Monday";
        case 2: return "Tuesday";
        case 3: return "Wednesday";
        case 4: return "Thursday";
        case 5: return "Friday";
        case 6: return "Saturday";
    }
}
