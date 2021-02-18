
# 策略代碼編輯器

## 一. 功能說明

### 1. 檔案操作

- 新增檔案 NewFile (Ctrl + N)
- 開啟檔案 OpenFile (Ctrl + O)
- 關閉檔案 CloseFile (Ctrl + C)
- 儲存檔案 SaveFile (Ctrl + S)
- 另存新黨 SaveAs 
- 匯出 Expert
- 匯入 Import 
- 編譯 Compile

### 2. 編輯操作
- 復原 Undo (Ctrl + Z)
- 取消復原 Redo
- 剪下 Cut (Ctrl + X)
- 複製 Copy (Ctrl + C)
- 貼上 Paste (Ctrl + V)
- 全選 SelectAll (Ctrl + A)
- 尋找 Find (Ctrl + F)
- 取代 Replace (Ctrl + H)



## 二. 介面需求

### 1. 檔案列表視窗 FileListWindow
檔案列表需可選取兩種模式, 分別為**樹狀顯示**及**列表顯示**
樹狀顯示使用**TreeWidget**
列表顯示使用**TableWidget**, 主要欄位為:
|檔案名稱|檔案描述|最後編輯時間|所在目錄|
|:--:|:--:|:--:|:--:|

### 2. 編輯器視窗 CodeEditWindow
主要提供使用者編寫代碼, 使用**CodeEdit** Class

### 3. 日誌視窗 LogWindow
主要提供使用者監控檔案編譯狀況及錯誤訊息

### 4. 狀態列 StatusBar 
主要用於顯示檔案的狀態 (是否儲存/是否編譯)

