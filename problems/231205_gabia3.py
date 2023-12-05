"""
당신은 실버를 사용해 골드를 사고파는 온라인 화폐 거래소를 운영합니다. 화폐 거래소를 이용하는 회원들은 알파벳 대소문자로 이루어진 고유한 아이디를 가지고 있습니다. 회원들은 화폐 거래소에 골드 구매 요청과 골드 판매 요청을 등록할 수 있으며, 완료되지 않은 요청은 pending, 완료된 요청은 done을 상태로 가집니다.

판매할 골드의 양이 sell_amount, 판매가격이 sell_price 인 골드 판매 요청 등록은 다음 과 같은 순서로 처리됩니다.

1. pending 상태인 구매 요청 중 구매 가격이 sell_price 이상인 구매 요청을 찾습니다. 그러한 구매 요청이 여러 개일 경우 구매 가격이 가장 비싼 구매 요청 중 가장 먼저 등록된 구매 요청을 선택합니다. 구매 가격이 Aell_price 이상인 구매 요청을 찾지 못했을 경우, 판매 요 청은 pending 상태가 되며 등록을 종료합니다.
2. 찾은 구매 요청의 구매 골드 양이 buy_amount 일 때, 골드 1당 sell_price 의 가격으로 min( buy_amount, sell_amount) 만큼의 골드 거래가 이루어집니다. 거래가 이루어진 골드의 양이 amount 라면, 판매자의 계좌에서 구매자의 계좌로 amount 만큼의 골드가 이동하며, 구매자의 계좌에서 판매자의 계좌로 amount x sell_price 만큼의 실버가 이동합니다.
3. 구매 요청의 buy_amount 가 min( buy_amount, sell_amount) 만큼 감소합니다. buy_amount 가 0이 되었다면 해당 구매 요청은 done 상태가 됩니다.
4. 판매 요청의 sell_amount 가 min(buy_amount,
sell_amount)만큼 감소합니다. sell_amount 가 0이 되었다면 해당 판매 요청은 done 상태가 되며, 등록을 종료합니다.
5. sell_amount 가 1 이상이라면 1번 순서로 돌아갑니다.
골드 구매 요청 또한 골드 판매 요청과 유사하게 처리됩니다. 구매할 골드의 양이 buy_amount, 구매 가격이 buy_price 인 골 구매 요청의 등록은 다음과 같은 순서로 처리됩니다.

1. pending 상태인 판매 요청 중 판매 가격이 buy_price 이하인 판 매 요청을 찾습니다. 그러한 판매 요청이 여러 개일 경우 판매 가격이 가 장 싼 판매 요청 중 가장 먼저 등록된 판매 요청을 선택합니다. 판매 가격 이 buy_price 이하인 판매 요청을 찾지 못했을 경우, 구매 요청은 pending 상태가 되며 등록을 종료합니다.
2. 찾은 판매 요청의 판매 골드 양이 sell_amount 일 때, 골드 1당 sell_price 의 가격으로 min( buy_amount, sell_amount)만 큼의 골드 거래가 이루어집니다. 거래가 이루어진 골드의 양이
amount 라면, 판매자의 계좌에서 구매자의 계좌로 amount 만큼의 골드가 이동하며, 구매자의 계좌에서 판매자의 계좌로 amount x sell_price 만큼의 실버가 이동합니다.
3. 판매 요청의 sell amount 가 min( buy_amount
sell amount)만큼 감소합니다. sell_amount 가 0이 되었다면 해당 판매 요청은 done 상태가 됩니다.
4. 구매 요청의 buy_amount 가 min( buy_amount, sell_amount) 만큼 감소합니다. buy_amount 가 0이 되었다면 해당 구매 요청은 done 상태가 되며, 등록을 종료합니다.
5. buy_amount 가 1 이상이라면 1번 순서로 돌아갑니다.

입출력 예시
req_id
["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"]

req_info
[[1,7,20], [0,10,10], [1,10,40], [1,4,25], [0,5,11], [0,20,30]]

result
["Andy +11 -240", "Louis 0 0", "Rohan -4 +100", "William -7 + 140"]
"""