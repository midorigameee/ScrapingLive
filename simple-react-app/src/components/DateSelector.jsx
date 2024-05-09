import { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import styles from "../cssModule/DateSelector.module.css";

export function DateSelector(props) {
  const [startDate, setStartDate] = useState(new Date());

  return (
    <>
      <label for="selectedDate">いつ？</label>
      <DatePicker
        id="selectedDate"
        selected={startDate}
        onChange={(date) => setStartDate(date)}
      />
    </>
  );
}
