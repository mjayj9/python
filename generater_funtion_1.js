// 1. 가상의 서버 API 호출 함수 (비동기 데이터 fetch 시뮬레이션)
const mockFetchItemsFromServer = (page) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            if (page > 3) {
                resolve([]); // 3페이지가 넘어가면 빈 배열 반환 (끝을 의미)
            } else {
                resolve([`데이터 A (현재 page: ${page})`, `데이터 B (현재 page: ${page})`]);
            }
        }, 800); // 0.8초 서버 대기 시간 시뮬레이션
    });
};

// 2. 완성형 페이지네이션 제너레이터 함수
async function* paginatedDataFetcher() {
    let currentPage = 1;

    while (true) {
        // 서버에서 현재 페이지 데이터 가져오기 (비동기 제어)
        const items = await mockFetchItemsFromServer(currentPage);

        // 가져올 데이터가 더 이상 없으면 제너레이터 종료
        if (items.length === 0) {
            console.log("▶ [알림] 모든 데이터를 호출 완료했습니다.");
            return;
        }

        // 데이터를 성공적으로 가져왔다면 호출한 곳으로 데이터 전달 후 일시 정지
        yield items;
        currentPage++;
    }
}

// 3. 실제 실행 및 흐름 제어 부분 (클라이언트 예시)
async function runAsyncApp() {
    const fetcherInstance = paginatedDataFetcher();

    console.log("--- 1번째 스크롤 다운 (1페이지 요청) ---");
    const res1 = await fetcherInstance.next();
    console.log("받은 데이터:", res1.value); // ['데이터 A (page: 1)', '데이터 B (page: 1)']

    console.log("\n--- 2번째 스크롤 다운 (2페이지 요청) ---");
    const res2 = await fetcherInstance.next();
    console.log("받은 데이터:", res2.value); // ['데이터 A (page: 2)', '데이터 B (page: 2)']

    console.log("\n--- 3번째 스크롤 다운 (3페이지 요청) ---");
    const res3 = await fetcherInstance.next();
    console.log("받은 데이터:", res3.value); // ['데이터 A (page: 3)', '데이터 B (page: 3)']

    console.log("\n--- 4번째 스크롤 다운 (더 이상 데이터 없음) ---");
    const res4 = await fetcherInstance.next();
    console.log("완료 여부(done):", res4.done); // true
}

runAsyncApp();
