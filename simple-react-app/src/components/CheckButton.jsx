import styles from "../cssModule/CheckButton.module.css";

export function CheckButton({ count, setCount }) {
  return (
    <>
      <button
        className={styles.ButtonStyle}
        onClick={() => setCount(count + 1)}
      >
        スケジュール確認
      </button>
    </>
  );
}
