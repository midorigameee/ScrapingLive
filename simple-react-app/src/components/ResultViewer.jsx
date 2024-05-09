import { useEffect, useState } from "react";
import { getLiveSchedule } from "../utils/getLiveSchedule";

export function ResultViewer({ count, targetDate }) {
  let [info, setInfo] = useState({});
  let [visible, setVisible] = useState(false);
  let [resResult, setResResult] = useState(false);
  let [loading, setLoading] = useState(true);

  const apiUrl = "http://localhost:5000/api/osaka/zepp-namba";

  useEffect(() => {
    info.result ? setResResult(true) : setResResult(false);
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
      const year = targetDate.getFullYear();
      const month = targetDate.getMonth() + 1;
      const day = targetDate.getDate();

      fetchLiveInfo(year, month, day);
      setVisible(true);
    };

    if (count !== 0) displaySchedule();
    setLoading(true);
  }, [count]);

  const formatResultJson = () => {
    return (
      <div>
        <div>地域：{info.area}</div>
        <div>会場：{info.site}</div>
        <div>アーティスト：{info.performer}</div>
        <div>イベント名：{info.title}</div>
      </div>
    );
  };

  const showResult = () => {
    return resResult ? formatResultJson() : "データがありません";
  };

  const loadJson = () => {
    return loading ? "読み込み中..." : showResult();
  };

  return (
    <>
      <div>{visible ? loadJson() : "ここにスケジュールが表示されます"}</div>
    </>
  );
}
