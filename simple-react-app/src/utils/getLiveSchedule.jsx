export const getLiveSchedule = (url) => {
  return new Promise((resolve, reject) => {
    // fetchでデータを取得 → resに格納してjsonにする → jsonにした値をdataに格納してresolveに詰めて返す（成功したよ、って意味で返す）
    fetch(url, {
      method: "GET",
      mode: "cors",
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then((data) => {
        // 空のJSONが返された場合の処理
        if (Object.keys(data).length === 0) {
          throw new Error("Empty JSON response");
        }
        resolve(data);
      })
      .catch((error) => {
        console.error("Fetch error:", error);
        reject(error); // エラーが発生した場合にrejectする
      });
  });
};
