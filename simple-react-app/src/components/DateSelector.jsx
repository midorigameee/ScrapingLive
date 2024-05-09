import { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import styles from "../cssModule/DateSelector.module.css";

export function DateSelector({ targetDate, setTargetDate }) {
  return (
    <>
      <label for="selectedDate">いつ？</label>
      <DatePicker
        id="selectedDate"
        selected={targetDate}
        onChange={(date) => setTargetDate(date)}
      />
    </>
  );
}
