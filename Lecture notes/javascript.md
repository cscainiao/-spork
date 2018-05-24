```
javascript   js   behavior
ECMAScript  语法规范  ES5
BOM  - 	浏览器对象模型 - window
DOM  - 文档对象模型
```

## 显示

```
document.getElementById("demo") 是使用 id 属性来查找 HTML 元素的 JavaScript 代码 。
innerHTML = "段落已修改。" 是用于修改元素的 HTML 内容(innerHTML)的 JavaScript 代码。

document.write() 仅仅向文档输出写内容。
如果在文档已完成加载后执行 document.write，整个 HTML 页面将被覆盖。

如果您的浏览器支持调试，你可以使用 console.log() 方法在浏览器中显示 JavaScript 值。
浏览器中使用 F12 来启用调试模式， 在调试窗口中点击 "Console" 菜单。
```

## 变量

```
JavaScript 使用关键字 var 来定义变量， 使用等号来为变量赋值：

变量必须以字母开头
变量也能以 $ 和 _ 符号开头（不过我们不推荐这么做）
变量名称对大小写敏感（y 和 Y 是不同的变量）

您可以在一条语句中声明很多变量。该语句以 var 开头，并使用逗号分隔变量即可：
```

## 语句标识符

```
break	用于跳出循环。
catch	语句块，在 try 语句块执行出错时执行 catch 语句块。
continue	跳过循环中的一个迭代。
do ... while	执行一个语句块，在条件语句为 true 时继续执行该语句块。
for	在条件语句为 true 时，可以将代码块执行指定的次数。
for ... in	用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。
function	定义一个函数
if ... else	用于基于不同的条件来执行不同的动作。
return	退出函数
switch	用于基于不同的条件来执行不同的动作。
throw	抛出（生成）错误 。
try	实现错误处理，与 catch 一同使用。
var	声明一个变量。
while	当条件语句为 true 时，执行语句块。
```

```
您可以在文本字符串中使用反斜杠对代码行进行换行。下面的例子会正确地显示：

注释:
单行注释以 // 开头。
多行注释以 /* 开始，以 */ 结尾.
```

```
如果变量 age 中的值小于 18，则向变量 voteable 赋值 "年龄太小"，否则赋值 "年龄已达到"。
voteable=(age<18)?"年龄太小":"年龄已达到";
self._working_hour = working_hour if working_hour > 0 else 0   python中用法
```

```
console.log() 
```

```
document 对象查找元素方法

document.getElementsByTagName
document.getElementsByClassName
document.querySelectorAll/querySelector
document.getElementsById

修改节点的内容和属性
textContent(文本)  innerHTML(带标签)  nodeValue
访问成员运算符(.)
setAttribute   getAttribute   removeAttribute

获得一个节点,访问其父节点,子节点,兄弟节点
parentNode(父节点)
children /firstChild/lastChild (子节点)
nextSibling /prevSibling
```

```
evt.preventDefault 阻止事件的默认行为
```

```
正则表达式30分钟入门教程 deerchao
```

```
jQuery.noConflict() 让出$函数以后原来用$函数的地方全部换成jQuery
```

```
循环里面要从数组里面删除元素的时候  要倒着循环   
```

