import styles from "../cssModule/SelectOptions.module.css";

export function SelectOptions(props) {
  const { startDate, endDate } = props;

  const createDateList = () => {
    let dateList = [];

    for (let d = startDate; d <= endDate; d.setDate(d.getDate() + 1)) {
      let fullDate = d.getFullYear() + "/" + d.getMonth() + "/" + d.getDate();
      dateList.push(fullDate);
    }
    return dateList;
  };

  const dateList = createDateList();

  return (
    <div className={styles.SelectOptionsContainer}>
      <div className={styles.SelectOptionsBox}>
        <label for="selectedArea">どこ？</label>
        <select id="selectedArea">
          <option value="tokyo">東京</option>
          <option value="nagoya">名古屋</option>
          <option value="osaka">大阪</option>
        </select>
      </div>
      <div className={styles.SelectOptionsBox}>
        <label for="selectedDate">いつ？</label>
        <select id="selectedDate">
          {dateList.map((date) => {
            return (
              <option key={date} value={date}>
                {date}
              </option>
            );
          })}
        </select>
      </div>
    </div>
  );
}
