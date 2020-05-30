# Logic for CS Project

- 李沛潔 107971023
- 邱柏森 107753029

## Schedule

- ***6/5***

	各組向老師報告目前進度與遭遇問題

- ***6/12***

	成果報告

- ***6/19***

	期末考！

## Checklist

- [ ] `fin_pairs.csv` 資料前處理

	- [x] 以 `dataset_parser.py` 解析其內容

	- [ ] 輸出成 prolog 的 knowledge bases

	- [ ] 設計 query

- [x] 建立 Prolog 執行環境 `solver.sh`

- [ ] 簡報製作

## Quick Start

***Run*** `sh solver.sh example`

## Problems

- `fin_pairs.csv` 原始檔出現 UnicodeDecodeError

	```
	UnicodeDecodeError: 'utf-8' codec can't decode bytes in position 53-54: invalid continuation byte
	```

- how to define predicates?

	> input sentence:
	>> whole sentence: “An apple a day, keeps a doctor away.”
		    ** cause: ”An apple a day”
		    ** effect: ”keeps a doctor away”

	> output of parsed pairs:
	>> whole sentence: exist apple exist day exist doctor exist (away,keeps) and exist (keeps,apple) and exist (keeps,doctor) and exist (apple,day)
		    ** cause: exist apple exist day exist (apple,day)
		    ** effect: exist doctor exist (away,keep) and exist (keep,doctor)

	> So we might get the relation (keeps,apple) => apple is the reason that makes you keep away doctor

    ```
    (away,keeps) (keeps,apple) (keeps,doctor) (apple,day)
	- atomic sentences:keeps(apple).
			   keeps(doctor).
		 	   day(apple).
	- relation(effect) :- relation(cause).
		condition sentence: away(X,Y) :- day(X), keeps(X), keeps(Y), \+ X=Y.
		query: ?- away(X,Y).
			X=apple
			Y=doctor
    ```
