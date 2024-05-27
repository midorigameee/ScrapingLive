import styles from "../cssModule/AreaSelector.module.css";

export function AreaSelector({ targetArea, setTargetArea }) {
  const areaList = [
    { value: "tokyo", name: "東京" },
    { value: "nagoya", name: "名古屋" },
    { value: "osaka", name: "大阪" },
  ];

  const useSetTargetArea = (event) => {
    setTargetArea(event.target.value);
  };

  return (
    <>
      <label for="selectedArea">どこ？</label>
      <select id="selectedArea" onChange={useSetTargetArea}>
        {areaList.map((area) => {
          return (
            <option key={area.value} value={area.value}>
              {area.name}
            </option>
          );
        })}
      </select>
    </>
  );
}
