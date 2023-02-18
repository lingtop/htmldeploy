#เราสามารถเพิ่มข้อมูลใน list ได้โดยการใช้คำสั่งดังนี้ append(), extend() (+=ก็สามารถใช่ได้เหมือนกัน)
'''
flowers = ['Rose', 'Lily', 'Tulip', 'Carnation', 'Poppy', 'Sunflower']
print(flowers)

flowers.append(['Iris'])
print(flowers)
flowers.extend(['Violet'])
print(flowers)
'''
#ส่วนการแก้ไขข้อมูล เราสามารถทำได้โดยการ เข้าถึงข้อมูลและ set ข้อมูลที่เราเข้าถึงเป็นข้อมูลที่เราต้องการได้ เช่น
'''
list1 = ['physics', 'chemistry', 'calculus', 'biology'];
print(list1)
list1[2] = 'programming';
print(list1)
'''
#ถ้าต้องการแทรก list ในตำแหน่งที่ต้องการให้ใช้ insert(ตำแหน่งที่จะแทรก, ข้อมูลที่จะแทรก)
'''motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles.insert(2, 'harley')
print(motorcycles)'''

#การลบข้อมูลใน List ทำได้หลายวิธี 
#clear เป็นการลบ list ทั้งหมด
#remove เป็นการลบโดยอ้างถึงค่า
#del, pop เป็นการลบโดยอ้างถึงตำแหน่ง
'''motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

print(motorcycles)

del motorcycles[2]
print(motorcycles)

motorcycles.pop(0)
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles.clear()
print(motorcycles)'''


