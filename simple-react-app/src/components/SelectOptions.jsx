export function SelectOptions(props) {
  const { startDate, endDate } = props;

  const createDateList = () => {
    // const startDate = new Date(2024, 5, 1);
    // const endDate = new Date(2024, 5, 31);
    let dateList = [];

    for (let d = startDate; d <= endDate; d.setDate(d.getDate() + 1)) {
      let fullDate = d.getFullYear() + "/" + d.getMonth() + "/" + d.getDate();
      dateList.push(fullDate);
    }
    return dateList;
  };

  const dateList = createDateList();

  return (
    <div>
      <label for="selectedDate">日付を選択</label>
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
  );
}
