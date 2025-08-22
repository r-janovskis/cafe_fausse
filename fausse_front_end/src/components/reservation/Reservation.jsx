import React, { useState, useEffect } from "react";

function Reservation() {
  // Declare states where we will keep track of the reservation booking
  // We will start with empty states
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [numberOfGuests, setNumberOfGuests] = useState("");
  const [newsletter, setNewsletter] = useState("false");

  // State where we will keep track of our available time slots
  const [timeSlots, setTimeSlots] = useState([]);

  function isSunday(dateToCheck) {
    return new Date(dateToCheck).getDay() === 0;
  }
  // Function that generates the reservation time slots
  function generateTimeSlots() {
    const timeSlots = [];

    // Variables that we will use to generate the time slots
    const step = 15;
    let start = 17;
    let end = 21;
    // If there is no date selected leave time options empty
    if (!date) {
      return [];
    }

    // Check if the selected date is a Sunday
    if (isSunday(date)) {
      // For sundays we are working shorter hours 5PM (17:00) - 9 PM (21:00)
      // As our reservation is for 2h slot we need options
      // 5PM (17:00) - 7 PM (19:00)
      end = 19;

      // We still need to check start time, so it's not earlier than the time we are currently at
      // And we take reservation only 2 hour in advance from current hour so that we have time to prepare
      // If he is booking at 16:55 then on the day he will be able to book only starting at 18:00
      if (date === today) {
        start = Date.now().getHours() + 2;
      }
    }

    // No slots left for the selected date (today)
    if (start >= end) {
      return [];
    }

    // Generate the time slots
    let currentTime = new Date();
    currentTime.setHours(start, 0, 0, 0);

    const endTime = new Date();
    endTime.setHours(end, 0, 0, 0);

    // We generate time slot for every 15 min
    while (currentTime <= endTime) {
      const hours = currentTime.getHours().toString().padStart(2, "0");
      const minutes = currentTime.getMinutes().toString().padStart(2, "0");
      const timeSlotEntry = {
        option: `${hours}:${minutes}`,
        value: `${hours}:${minutes}:00`,
      };
      timeSlots.push(timeSlotEntry);
      currentTime.setMinutes(currentTime.getMinutes() + step);
    }

    return timeSlots;
  }

  function onChangeDate(event) {
    setDate(event.target.value);
  }

  function onChangeTime(event) {
    setTime(event.target.value);
  }

  function onChangeName(event) {
    setName(event.target.value);
  }

  function onChangeEmail(event) {
    setEmail(event.target.value);
  }

  function onChangePhoneNumber(event) {
    setPhoneNumber(event.target.value);
  }

  function onChangeNumberOfGuests(event) {
    setNumberOfGuests(event.target.value);
  }

  function onChangeNewsletter(event) {
    setNewsletter(event.target.value);
  }

  // function to submit a reservation request
  // Or in simple terms -> book a table
  function submitReservation() {
    console.log({
      date,
      time,
      name,
      email,
      phoneNumber,
      numberOfGuests,
      newsletter,
    });
  }

  // We will restric reservations to be booked only from the current day forward
  const today = new Date().toISOString().split("T")[0];

  useEffect(() => {
    const newTimeSlots = generateTimeSlots();
    setTimeSlots(newTimeSlots);

    console.log(newTimeSlots);
  }, [date]);

  return (
    <div>
      <h2> Book a table!</h2>
      <form onSubmit={submitReservation}>
        <label htmlFor="date">Date</label>
        <input
          type="date"
          id="date"
          name="date"
          min={today}
          onChange={onChangeDate}
        />
        <label htmlFor="time">Time</label>
        <select name="time" id="time">
          {timeSlots.map((timeSlot) => (
            <option value={`${timeSlot.value}`}>{timeSlot.option}</option>
          ))}
        </select>
      </form>
    </div>
  );
}

export default Reservation;
