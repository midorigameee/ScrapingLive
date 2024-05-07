import { useEffect, useState } from "react";
import { getLiveSchedule } from "./utils/getLiveSchedule";
import { SelectOptions } from "./components/SelectOptions";

function App() {
  let [info, setInfo] = useState({});
  let [visible, setVisible] = useState(false);
  let [count, setCount] = useState(0);
  let [result, setResult] = useState(false);
  let [loading, setLoading] = useState(true);

  const apiUrl = "http://localhost:5000/api/osaka/zepp-namba";

  useEffect(() => {
    info.result ? setResult(true) : setResult(false);
  }, [info]);

  /*
  ボタンが押されたときにfetchしてInfoを更新する
   */
  useEffect(() => {
    const fetchLiveInfo = async (year = "", month = "", day = "") => {
      const apiUrlWithParam = `${apiUrl}?year=${year}&month=${month}&day=${day}`;
      console.log(`apiUrlWithParam: ${apiUrlWithParam}`);
      let res = await getLiveSchedule(apiUrlWithParam);

      setInfo(res);
      setLoading(false);
    };

    const displaySchedule = () => {
      const selectedDate = document.getElementById("selectedDate").value;
      const [year, month, day] = selectedDate.split("/");

      fetchLiveInfo(year, month, day);
      setVisible(true);
    };

    if (count !== 0) displaySchedule();
    setLoading(true);
  }, [count]);

  const viewJson = () => {
    return loading ? (
      "読み込み中..."
    ) : result ? (
      <div>
        <div>地域：{info.area}</div>
        <div>会場：{info.site}</div>
        <div>アーティスト：{info.performer}</div>
        <div>イベント名：{info.title}</div>
      </div>
    ) : (
      "スケジュールがありません"
    );
  };

  const startDate = new Date(2024, 5, 1);
  const endDate = new Date(2024, 5, 31);

  return (
    <>
      <h1>Live schedule</h1>
      <SelectOptions startDate={startDate} endDate={endDate} />
      <button onClick={() => setCount((prev) => prev + 1)}>Get schedule</button>
      <div>{visible ? viewJson() : "ここにスケジュールが表示されます"}</div>
    </>
  );
}

export default App;
