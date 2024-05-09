import styles from "../cssModule/Title.module.css";

export function Title() {
  return (
    <h1 className={styles.TitleStyle}>
      <div className={styles.TitleLine}>ライブ行こうぜ!!</div>
    </h1>
  );
}
