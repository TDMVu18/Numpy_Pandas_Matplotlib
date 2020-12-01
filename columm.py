import matplotlib.pyplot as plt
 

A = {'2020': 10, '2017': 20, '2007': 50, '2015': 30, '2010': 40} 
Counts = sorted(A.values(), reverse=True)
Foods = sorted(A, key=A.__getitem__, reverse=True) 
ind_Foods= range(len(A))
plt.bar(ind_Foods, Counts, align='center')
plt.xticks(ind_Foods, Foods)
 

plt.xlabel('Càng ngày càng xấu')
plt.ylabel('Count (like)')

plt.title('ĐỘ ĐẸP TRAI CỦA VŨ THEO TỪNG NĂM') 
for x, y in zip(ind_Foods, Counts):
    plt.text(x+0.02, y+0.05, '%d' % y, ha='center', va= 'bottom')
 
plt.ylim(0, Counts[0] + 20)
 
# Cuối cùng là show kết quả!!!
plt.show()
