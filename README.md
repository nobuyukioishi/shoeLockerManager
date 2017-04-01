# shoeLockerManager
for applications

## 構造
We use 4 pipeline stages to get result.  See below

Pipeline:
1. getImage
2. dissembler
3. imageRecognize
4. saveResult    

### Functions input and outputs:
functionName(Input : type) -> Output : type

1. getImage( NULL ) -> BigImage : JPG file
2. dissembler(BigImage ) ->  {'id':integer , 'Shoe':numpy array} : dictionary
3. imageRecognize(  {'id':integer , 'Shoe':numpy array} ) -> {'id':integer , 'isShoe':bool} : dictionary
4. saveResult( {'id':integer , 'isShoe':bool}) -> ...

Notice:
1. id in imageRecognize and saveResult are same array.
2. dissembler can save images in jpg for debugging.

