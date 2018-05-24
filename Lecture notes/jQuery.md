查找元素

- 选择器
  - * / element / #id / .class / selector1, selector2
  - ancestor descendant / parent>child / previous+next / previous~siblings 
- 筛选器
  - 基本筛选器：:not(selector) / :first / :last / :even / :odd / :eq(index) / :gt(index) / :lt(index) / :animated / :focus
  - 内容筛选器：:contains('…') / :empty / :parent / :has(selector)
  - 可见性筛选器：:hidden / :visible
  - 子节点筛选器：:nth-child(expr) / :first-child / :last-child / :only-child
  - 属性筛选器：[attribute] / [attribute='value'] / [attribute!='value'] / [attribute^='value'] / [attribute$='value'] / [attribute|='value'] / [attribute~='value']
- 表单：:input / :text / :password / :radio / :checkbox / :submit / :image / :reset / :button / :file / :selected / :enabled / :disabled / :checked

执行操作

- 内容操作
  - 获取/修改内容：html() / text() / replaceWith() / remove()
  - 获取/设置元素：before() / after() / prepend() / append() / remove() / clone() / unwrap() / detach() / empty() / add()
  - 获取/修改属性：attr(){修改标签里面属性} / removeAttr() / addClass() / removeClass() / css(){修改css层叠样式表}
  - 获取/设置表单值：val()
- 查找操作
  - 查找方法：find() /  parent() / children() / siblings() / next() / nextAll() / prev() / prevAll()
  - 筛选器：filter() / not() / has() / is() / contains()
  - 索引编号：eq()
- 尺寸和位置
  - 尺寸相关：height() / width() / innerHeight() / innerWidth() / outerWidth() / outerHeight()
  - 位置相关：offset() / position() / scrollLeft() / scrollTop()
- 特效和动画
  - 基本动画：show() / hide() / toggle()
  - 消失出现：fadeIn() / fadeOut() / fadeTo() / fadeToggle()
  - 滑动效果：slideDown() / slideUp() / slideToggle()
  - 自定义：delay() / stop() / animate()
- 事件
  - 文档加载：ready() / load()
  - 用户交互：on() / off()

```
jQuery里面css传一个参数是读数据    穿两个数据表示改样式
```

```
jQueryUi 插件   http://www.bootcdn.cn/
www.jqueryui.org.cn
```

```
ajax 
```

```
layoutit 可视化布局  快速布局页面
```

