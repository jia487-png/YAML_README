# YAML_README
YAML文件语法解析及读取

YAML 是 "YAML Ain't a Markup Language"（YAML 不是一种标记语言）的递归缩写。在开发的这种语言时，YAML 的意思其实是："Yet Another Markup Language"（仍是一种标记语言）。

# 重点

## YAML完全兼容JSON格式，并且支持PYTHON语言相似写法
## 是数据格式，不是编程语言
## 像PYTHON一样容易编辑和阅读

# 基本语法

大小写敏感
使用缩进表示层级关系,缩进的空格数不重要，只要相同层级的元素左对齐即可
缩进不允许使用 tab，只允许空格
 '#' 表示注释
：冒号和‘-’后的值要加一个空格

数据类型
YAML 支持的数据结构有三种：

对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
纯量（scalars）：单个的、不可再分的值

## 1. 基本语法规则
### 1.1. 缩进与空白
缩进：YAML 使用空格来表示层级结构，建议每层使用 2 或 4 个空格，不允许使用制表符（Tab）。
空行：可以使用空行来分隔不同部分，提高可读性。


### 1.2. 注释
注释以 # 开头，# 后面的内容将被忽略。例如：
‘#’ 这是一个注释
key: value  # 行尾注释

### 1.3. 数据类型
字符串：可以直接写字符串，若字符串中包含特殊字符或空格，可用引号包围（单引号或双引号）。
数字：直接写数字即可。
布尔值：可以使用 true 或 false（大小写敏感，推荐全部小写）。
Null：使用 null 或 ~ 表示空值。

纯量是最基本的，不可再分的值，包括：

字符串
布尔值
整数
浮点数
Null
时间
日期

~~~~
boolean: 
    - TRUE  #true,True都可以
    - FALSE  #false，False都可以
float:
    - 3.14
    - 6.8523015e+5  #可以使用科学计数法
int:
    - 123
    - 0b1010_0111_0100_1010_1110    #二进制表示
null:
    nodeName: 'node'
    parent: ~  #使用~表示null
string:
    - 哈哈
    - 'Hello world'  #可以使用双引号或者单引号包裹特殊字符
    - newline
      newline2    #字符串可以拆成多行，每一行会被转化成一个空格
date:
    - 2018-02-17    #日期必须使用ISO 8601格式，即yyyy-MM-dd
datetime: 
    -  2018-02-17T15:02:31+08:00    #时间使用ISO 8601格式，时间和日期之间使用T连接，最后使用+代表时区
~~~~

## 2. 数据结构表示
### 2.1. 映射（字典）
使用键值对表示映射，冒号 : 后面必须跟一个空格。

~~~~
person:
  name: John Doe
  age: 30
  married: true
~~~~

### 2.2. 序列（列表）
有两种常见的表示方式：

方式一：使用短横线
~~~~
fruits:
  - apple
  - banana
  - cherry
~~~~

方式二：使用内联表示法
~~~~
fruits: [apple, banana, cherry]
~~~~

### 2.3. 嵌套结构
可以将映射和序列任意嵌套：
~~~~
employees:
  - name: Alice
    skills:
      - Python
      - JavaScript
  - name: Bob
    skills:
      - Go
      - Rust
~~~~

## 3. 复杂数据类型
### 3.1. 多行字符串
YAML 提供两种方式处理多行字符串：

保留换行（literal style）
使用竖线 |，换行符会被保留：
~~~~
description: |
  这是一个多行字符串示例。
  每一行都会被保留换行符。
~~~~

折叠换行（folded style）
使用大于号 >，换行会被折叠为空格：

~~~~
summary: >
  这是一个折叠多行字符串示例，
  所有换行都会被折叠为空格，
  形成一行长字符串。
~~~~

### 3.2. 锚点与别名
YAML 支持复用数据，通过锚点（&）定义和别名（*）引用：

& 锚点和 * 别名，可以用来引用:
~~~~
defaults: &defaults
  adapter:  postgres
  host:     localhost
 
development:
  database: myapp_development
  <<: *defaults
 
test:
  database: myapp_test
  <<: *defaults
~~~~

相当于:
~~~~
defaults:
  adapter:  postgres
  host:     localhost
 
development:
  database: myapp_development
  adapter:  postgres
  host:     localhost
 
test:
  database: myapp_test
  adapter:  postgres
  host:     localhost
~~~~

& 用来建立锚点（defaults），<< 表示合并到当前数据，* 用来引用锚点。

下面是另一个例子:
~~~~
- &showell Steve 
- Clark 
- Brian 
- Oren 
- *showell 
~~~~

转为yaml内联格式如下:
~~~~
[ 'Steve', 'Clark', 'Brian', 'Oren', 'Steve' ]
~~~~

## 4. 特殊语法
### 4.1. 内联映射
适合简单的键值对，可以写成一行：
~~~~
point: { x: 10, y: 20 }
~~~~

### 4.2. 内联序列
同样也可以在一行内表示列表：
~~~~
colors: [red, green, blue]
~~~~

### 4.3. 复合键
如果键包含特殊字符或空格，需要用引号包围：
~~~~
"first name": John
"last name": Doe
~~~~

## 5.json与yaml对比

json 中同样也会有对象和数组结构，这里我们做个简单的对比，通过下面的示例：

json 结构：
~~~~
{
  "apiVersion": "v1",
  "kind": "Pod",
  "metadata": {
        "name": "xx"
  }
  "spec": {
        "containers": [{
            "name": "front-end",
            "image": "nginx",
            "ports": [{
                "containerPort": "80"
            }]
        }, {
            "name": "flaskapp-demo",
            "image": "jcdemo/flaskapp",
            "ports": [{
                "containerPort": "5000"
            }]
        }]
  }
}
~~~~
如果我们把上面的结构用 yaml 表示，那么会是下面的结构：
~~~~
---
apiVersion: v1
kind: Pod
metadata:
  name: xx
spec:
  containers:
    - name: front-end
      image: nginx
      ports:
        - containerPort: 80
    - name: flaskapp-demo
      image: jcdemo/flaskapp
      ports:
        - containerPort: 80
~~~~

## 6. 常见错误及调试技巧
缩进错误：YAML 对缩进非常敏感，混用制表符和空格可能导致解析错误。建议统一使用空格。
冒号后的空格：键值对中的冒号后必须跟空格，否则解析器可能会报错。
特殊字符处理：对于包含冒号、逗号或其它特殊符号的字符串，建议使用引号包围。
调试 YAML 文件时，可以使用在线 YAML 校验工具或编程语言的 YAML 解析库来检测错误。


## 7、安装yaml
pip install pyyaml

