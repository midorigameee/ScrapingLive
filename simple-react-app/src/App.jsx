import { useState } from "react";
import styles from "./cssModule/App.module.css";
import { Title } from "./components/Title";
import { CheckButton } from "./components/CheckButton";
import { ResultViewer } from "./components/ResultViewer";
import { AreaSelector } from "./components/AreaSelector";
import { DateSelector } from "./components/DateSelector";

function App() {
  const [count, setCount] = useState(0);
  const [targetDate, setTargetDate] = useState(new Date());

  return (
    <div className={styles.AppStyle}>
      <Title />
      <AreaSelector />
      <DateSelector
        targetDate={targetDate}
        setTargetDate={(date) => setTargetDate(date)}
      />
      <CheckButton count={count} setCount={(num) => setCount(num)} />
      <ResultViewer count={count} targetDate={targetDate} />
    </div>
  );
}

export default App;
