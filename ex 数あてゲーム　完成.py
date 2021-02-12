# coding:utf-8
import random 
import tkinter as tk
import tkinter.messagebox as tsmg

a=[random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9)]


#ボタンがクリックされた時の処理
def ButtonClick():
    #テキスト入力された文字列を習得
    b=editbox1.get()

    isok=False
    if len(b) !=4:
        tsmg.showerror("エラー","4桁の数字を入力してください")
    else:    
        kazuok=True
        for i in range(4):
            if(b[i]<"0") or (b[i]>"9"):
                tsmg.showerror("エラー","数字ではありません")
                kazuok=False
                break
        if kazuok:
            isok=True

    if isok:
        hit=0
        for i in range(4):
            if a[i]==int(b[i]):
                hit=hit+1

        blow=0
        for j in range(4):
            for i in range(4):
                if(int(b[j])==a[i])and(a[i] !=int(b[i]))and(a[j] !=int(b[j])):
                    blow=blow+1
                    break
        if hit==4:
            tsmg.showinfo("当たり","おめでとうございます。あたりです")
            root.destroy()
        else:
            tsmg.showinfo("ヒント","ヒット"+str(hit)+"/"+"ブロー"+str(blow))
            rikibox.insert(tk.END,b+"    /H:"+str(hit)+"B:"+str(blow)+"            ")
            

print(a)

#メインのプログラム
#ウィンドウを作る
root=tk.Tk()
root.geometry("600x400")
root.title("数あてゲーム")

#ラベルを作る
labell=tk.Label(root,text="数を入力してね",font=("Helvetica",14))
labell.place(x=20,y=20)

#テキストボックスを作る
editbox1=tk.Entry(width=4,font=("Helvetica",28))
editbox1.place(x=120,y=60)

#ボタンを作る
button1=tk.Button(root,text="チェック",font=("Helvetica",14),command=ButtonClick)
button1.place(x=220,y=60)

#余白の作成
rikibox=tk.Text(root,font=("Helvetica",14))
rikibox.place(x=400,y=0,width=200,height=400)




#ウィンドウを表示する
root.mainloop()

