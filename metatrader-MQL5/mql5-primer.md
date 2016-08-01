# MQL5 Primer

## MQL Programs

* Expert Advisors - Automated trading program to open, close and modify orders. 1 Per Chart.
* Indicators - Displays technical analysis data. Many per chart.
* Scripts - Specialised program for specific task. 1 Per chart can only execute once.

## File Extensions

* .mq5 - source code opened with metaeditor
* .ex5 - compiled executable
* .mqh - include file with source code
* .set - settings and parameters

## Opening Metaeditor

1. Open Metatrader
2. Click the `MetaEditor` button or press `f4`

## Using Wizard

1. In metaeditor click `New`

## Syntax

* Every statement must end with a semicolon `;`
* Variables are `case sensitive`
* Comments: single line `//`, multiline `/* ... */`

**Metatrader shortcut:** `Edit -> Comments -> Comment Lines`

* Strongly typed (You need to explicitly declare datatype)
* If you don't specify initial value it will be `0` for numeric, `null` for text

## Data Types

### Integer types

#### Signed

* `char` : 1 byte [-128 to 127]
* `short` : 2 bytes [-32,768 to 32,767]
* `int` : 4 bytes [-2,147,483,648 to  2,147,483,647]
* `long` : 8 bytes [9,223,372,036,854,775,808 to 9,223,372,036,854,775,807]

#### Unsigned

* `uchar` : [0 to 255]
* `ushort` : [0 to 65,535]
* `uint` : [0 to 4,294,967,295]
* `ulong` : [0 to 18,446,744,073,709,551,615]

### Real types

* `float` : 4 bytes [accurate to 7 significant digits]
* `double` : 8 bytes [accurate to 15 significant digits]

### Strings

* `string`: escape with `\`, concatenate with `+`

### Boolean

* `bool`: `true` or `false`

### Color

* `color`: RGB colours - `clrRed`, `C'255,0,0'` or `0xFF0000`

### Datetime

* `datetime`: uses unix time

Specify a `datetime` constant

```
//format: yyyy.mm.dd hh:mm:ss

datetime myDate = D'2012.01.01 00:00:00';

//today's date
datetime myDate = D'';
```

## Constants

Value does not change

```
#define COMPANY_NAME "Easy Expert Forex"

or

const int cVar = 1;
```

## Arrays

```
int myArray[3];
myArray[0] = 1;
myArray[1] = 2;
myArray[2] = 3;

or

int myArray[3] = {1,2,3};
```

**Static arrays cannot be resized**

```
//Dynamic array
double myDynamic[];
ArrayResize(myDynamic,3);
myDynamic[0] = 1.50;
```

```
//Multidimensional arrays
double myDimension[3][3];
myDimension[0][1] = 1.35;
```

### Iterating through arrays

```
string myArray[3] = {"cheese","bread","ale"};
for(int index = 0; index < 3; index++)
{
   Print(myArray[index]);
}
```

```
int myDynamic[];
ArrayResize(myDynamic,10);
int size = ArraySize(myDynamic);
for(int i = 0; i < size; i++)
{
    myDynamic[i] = i;
    Print(i);
// Output: 0, 1, 2... 9
}
```

## Enums (Oh god)

```
enum DayOfWeek
        {
           Sunday,
           Monday,
           Tuesday,
           Wednesday,
           Thursday,
           Friday,
           Saturday,
};
```

## Structures

A structure is a set of related variables of different types.

```
struct tradeSettings
       {
           ulong slippage;
           double price;
           double stopLoss;
           double takeProfit;
           string comment;
};
```

```
tradeSettings trade;
trade.slippage = 50;
trade.stopLoss = StopLoss * _Point;
```

Standard structure `MqlTick`:

```
struct MqlTick
{
   datetime time; // Time of the last prices update
   double bid; // Current Bid price
   double ask; // Current Ask price
   double last; // Price of the last deal (Last)
   ulong volume; // Volume for the current Last price
};
```

Using `MqlTick`:

```
MqlTick price;
SymbolInfoTick(_Symbol,price);
Print(price.bid); // Returns the current Bid price
```

## Type Casting

`(int) difference`

## Input variables

The input variables of an MQL5 program are the only variables that can be changed by the user. These variables consist of trade settings, indicator settings, stop loss and take profit values, and so on. They are displayed under the Inputs tab of the program's Properties window.

```
input int MAPeriod = 10; // Moving average period
input ENUM_MA_METHOD MAMethod = MODE_SMA; // Moving average method
input double StopLoss = 20; // Stop loss (points)
input string Comment = "ea"; // Trade comment
```

## Predefined Variables

* `_Symbol` – The symbol of the financial security on the current chart.
* `_Period` – The period, in minutes, of the current chart.
* `_Point` – The point value of the current symbol. For five-digit Forex currency pairs, the point value is 0.00001, and for three-digit currency pairs (JPY), the point value is 0.001.
* `_Digits` – The number of digits after the decimal point for the current symbol. For five-digit Forex currency pairs, the number of digits is 5. JPY pairs have 3 digits.

## Source:

* MQL5Book
