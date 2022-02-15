\begin{code}
module A1_daij24 where -- Mentioned in the lecture (necessary for function calls)
matches :: Eq a => a -> [a] -> [a] -- given fucntion types
matches x [] = [] -- x cannot be an element of an empty list, so no matches
matches x y = if x == head y -- if x matches with the first element
   then [x] ++ matches x (tail y) -- then mtached element will be added into output list
else matches x (tail y) -- or we check later elements' matching
\end{code}

\begin{code}
element :: Eq a => a -> [a] -> Bool -- given fucntion types
element x [] = False -- x cannot be an element of an empty list, so false
element x y = if x == head y -- if x matches with the first element
   then True -- then return True
else element x (tail y) -- Or it checks later elements' matching
\end{code}

\begin{code}
pos :: Eq a => a -> [a] -> [Integer]-- given fucntion types
pos x [] = [] -- x cannot be an element of an empty list, so no matches
pos x y = if x == last y -- If element matches final element
   then pos x (init y) ++ [toInteger (length y) - toInteger 1] -- then match element's index will be added to output list
else pos x (init y) -- Or check earlier parts
\end{code}

\begin{code}
-- In my opinion, function "pos" is the best function on these functions.
-- According to pattern matching, all these 3 functions check all elements in the input list (array).

-- According to if-and-else, these functions have different if-and-else 
-- If fucntion "matches" finds a match, then it will add this matched value to output list, or it will do nothing.
-- If function "element" finds a match, then it will add true to output list, or it will continue check the next element.
-- If fucntion "pos" finds a match, then it will add this matched value's index to output list, or it will do nothing.
-- Compared with function "element", function "matches" and "pos" do not do anything when elements do not match.
-- But all of those 3 functions finds amount of matchs. And fucntion "matches" and "pos" do less work.
-- As a result, function "matches" and "pos" have advantages of finding amount of matched elements.

-- According to list comprehension, list is an ordered data type, so finding sequence (index) of matched elements are important.
-- If fucntion "matches" finds a match, then it will add this matched value to output list, or it will do nothing.
-- If function "element" finds a match, then it will add true to output list, or it will continue check the next element. If no matches then false
-- If fucntion "pos" finds a match, then it will add this matched value's index to output list, or it will do nothing.
-- We can see that only function "pos" shows the index of matched elements, and function "matches" does not show that.
-- So function "pos" have advantage of finding indexes of matched elements.

-- The only function has both advantages is the function "pos", so function "pos" is the "best" function.
\end{code}

\begin{code}
applyAll :: [a -> b] -> [a] -> [b] -- given function types
applyAll [] y = [] -- If list x is empty, then the multi-product has length 0, so empty list again
applyAll x [] = [] -- If list y is empty, then the multi-product has length 0, so empty list again
applyAll x y = map (head x) y ++ applyAll (tail x) y -- Apply each element in the 
\end{code}

\begin{code}
tripleNeg1 :: (Ord a , Num a) => [a] -> [a] -- given function types
tripleNeg1 [] = [] -- Empty list does not have nums to work with, so it does not change
tripleNeg1 x = if head x < 0 -- If first element is a negative number
   then [(head x) * (3)] ++ tripleNeg1 (tail x) -- Then we update this element (* 3) to output list
else [(head x)] ++ tripleNeg1 (tail x) -- Else numbers will be directly moved to output list

tripleNeg2 :: (Ord a , Num a) => [a] -> [a] -- given function types
tripleNeg2 [] = [] -- Empty list does not have nums to work with, so it does not change
tripleNeg2 x = map evalnum (eitherNeg2 x) -- map all values of either parts to output list

eitherNeg2 :: (Ord a , Num a) => [a] -> [Either a a] -- given function types
eitherNeg2 [] = [] -- Empty list does not have nums to work with, so it does not change
eitherNeg2 x = if head x < 0 -- check whether x is a negative number or not
   then [Left (head x)] ++ eitherNeg2 (tail x) -- Put negative numbers into Left either
else [Right (head x)] ++ eitherNeg2 (tail x) -- Put non-negative numbers into Right either

evalnum :: (Num a, Ord a) => Either a a -> a -- given function types
evalnum (Left n) = 3 * n -- if Left n then return 3 * n
evalnum (Right n) = n -- if Right n then return n
\end{code}

\begin{code}
data OrBoth a b = This a | That b | Both a b -- data type Orboth: This a (a), That b (b) and Both a b (both)
consume1 :: (a -> c) -> (b -> c) -> (a -> b -> c) -> OrBoth a b -> c -- given function types
consume1 f g h (This a) = f a -- If This a then apply function f on OrBoth
consume1 f g h (That b) = g b -- If That b then apply function g on OrBoth
consume1 f g h (Both a b) = h a b -- If Both a b then apply function h on OrBoth

consume2 :: (a -> c) -> (b -> c) -> (c -> c -> c) -> OrBoth a b -> c -- given function types
consume2 f g h (This a) = h (f a) (f a) -- If This a then apply function f on OrBoth, by using f output value, we have function h calling as output
consume2 f g h (That b) = h (g b) (g b) -- If That b then apply function g on OrBoth, by using g output value, we have function h calling as output
consume2 f g h (Both a b) = h (f a) (g b) -- If Both a b then apply function f and g on OrBoth, by using f and g output value, we have function h calling as output
\end{code}

\begin{code}
-- I think function "consume2" is better.
-- Because compared with function "consume1", it uses all inputs in all of its cases.
-- And it builds relationship between 3 different input functions, that is, one function use the result from other 2 functions.
-- And we can see that function h is used always
\end{code}

\begin{code}
data Ternary a = TLeaf a | TNode (Ternary a) (Ternary a) (Ternary a) -- given data types
mirror :: Ternary a -> Ternary a -- given function types
mirror (TLeaf x) = TLeaf x -- Individual TLeaf objects are symmetry and there is no need for mirror 
mirror (TNode x y z) = TNode (mirror z) y (mirror x) -- 2 sides of TNode 

flattenTernary :: Ternary a -> [a] -- given function types
flattenTernary (TLeaf x) = [x] -- For Individual TLeaf objects we just extract its number
flattenTernary (TNode x y z) = (flattenTernary x) ++ (flattenTernary y) ++ (flattenTernary z) -- For nodes we extract all of its 3 parts
\end{code}

\begin{code}
-- all :: (a -> Bool) -> [a] -> Bool
-- all p [] = True                     -- all.1
-- all p (x: xs) = p x && all p xs     -- all.2

-- Base Case: []
-- Our goal is all p ([] ++ ys) = all p [] && all p ys
-- LHS:
--    all p ([] ++ ys)                 by identity of ++
--  = all p ys
--
-- RHS:
--    all p [] && all p ys             by all.1
--  = true && all p ys                 by identity of +
--  = all p ys
-- Therefore our base case holds since our LHS = RHS!!
--
-- Induction Step:
-- Our goal is all p ((x:xs) ++ ys) = all p (x:xs) && all p ys
-- LHS:
--    all p ((x: xs) ++ ys)            by ++.2
--  = all p (x: (xs ++ ys))            by all.2
--  = p x && all p (xs ++ ys)
--
-- RHS:
--    all p (x:xs) && all p ys         by all.2
--  = p x && all p xs && all p ys      by induction hypothesis
--  = p x && all p (xs ++ ys)
-- Therefore our induction step holds since our LHS = RHS!!
\end{code}

\begin{code}
-- Assume input list xs and ys has equal length
mystery :: (a -> a -> a) -> [a] -> [a] -> [a] -- given function types
mystery f [] [] = [] -- if input number list 1 and 2 are both empty, there is no data pair we can do with given function
mystery f xs ys = [f (head xs) (head ys)] ++ mystery f (tail xs) (tail ys)
-- Extract first element of both input lists and 
\end{code}

\begin{code}
reverse :: [a] -> [a] -- Given function types
reverse [] = [] -- If empty list then do nothing (already reverse)
reverse [x] = [x] -- If list with one element then do nothing (already reverse)
reverse x = foldr (\y z -> (z ++ [y])) [] x -- If input list is complex then use foldr with reverse lambda function to reverse the whole list
-- Get help from lambda function tutorials
-- 1. https://stackoverflow.com/questions/22220439/haskell-lambda-expression
-- 2. https://www.tutorialspoint.com/haskell/haskell_functions.htm
\end{code}

\begin{code}
data Tree a = Tip | Node (Tree a) a (Tree a) deriving Show -- given data types
mirrorTree :: Tree a -> Tree a -- given function types
mirrorTree Tip = Tip -- Tip is symmetry, which means reverse Tip = Tip
mirrorTree (Node l a r) = Node (mirrorTree r) a (mirrorTree l) -- Exchange the left and right part and then have recursions on those sub parts

pre :: Tree a -> [a] -- given function types
pre Tip = [] -- Tip does not contain any node so return empty list
pre (Node l c r) = pre l ++ [c] ++ pre r -- check tree branch in all sub parts and connects them together

post :: Tree a -> [a] -- given function types
post Tip = [] -- Tip does not contain any node so return empty list
post (Node l c r) = post r ++ [c] ++ post l-- check tree branch in all sub parts and connects them together (in reverse order)
\end{code}

\begin{code}
-- mirrorTree :: Tree a -> Tree a
-- mirrorTree Tip = Tip                                              -- mirrorTree.1
-- mirrorTree (Node l a r) = Node (mirrorTree r) a (mirrorTree l)    -- mirrorTree.2
--
-- pre :: Tree a -> [a]
-- pre Tip = []                                                      -- pre.1
-- pre (Node l c r) = pre l ++ [c] ++ pre r                          -- pre.2
--
-- post :: Tree a -> [a]
-- post Tip = []                                                     -- post.1
-- post (Node l c r) = post r ++ [c] ++ post l                       -- post.2
--
-- reverse :: [a] -> [a]
-- reverse [] = []                                                   -- reverse.1
-- reverse (x: xs) = reverse xs ++ [x]                               -- reverse.2
-- reverse (xs ++ ys) = reverse (xs) ++ reverse (ys)                 -- theorem 1 (Have been proved in the tutorial 1)
-- 
-- Induction step: Tip
-- Our goal is pre (mirrorTree (Node l c r)) = reverse (post (Node l c r))
-- LHS:
--    pre (mirrorTree (Node l c r))                         by mirrorTree.2
--  = pre (Node (mirrorTree r) c (mirrorTree l))            by pre.2
--  = pre (mirrorTree r) ++ [c] ++ pre (mirrorTree l)
--
-- RHS:
--    Assume xs = post r, ys = post l      
--    reverse (post (Node l c r))                           by post.2
--  = reverse (post r ++ [c] ++ post l)                     by reverse.2
--  = reverse (xs ++ (ys: c))                               by theorem 1
--  = reverse xs ++ reverse (ys: c)                         by ++.2
--  = reverse xs ++ [c] ++ reverse ys                       by induction hypothesis
--  = pre (mirrorTree r) ++ [c] ++ pre (mirrorTree l)
-- Therefore our induction steps holds since our LHS = RHS!!
\end{code}

\begin{code}
data Rose a = Rose a [Rose a] deriving Show -- given data types
data Fork a = Leaf a | Branch (Fork a) (Fork a) deriving Show -- given data types

to' :: Tree a -> [Rose a] -- given function types
to' Tip = [] -- Tip (in Tree data type) do not have and node and this is empty list in rose
to' (Node l c r) = [Rose c ([] ++ to' l)] ++ to' r -- Left part is inside Rose data type list inside
-- Right part is Rose right part

from' :: [Rose a] -> Tree a -- given function types
from' [] = Tip -- Empty list represents Tree tip
from' [Rose a []] = Node Tip a Tip -- rule 1: Rose a [] is a single tree branch (both sides are empty)
from' [Rose a x] = Node (from' x) a Tip -- rule 2: any content is rose sub lists are developments on its left side
from' x = from2' (head x) (tail x) -- rule 3: devide x list in 2 parts, to distinguish left and right sides

from2' :: Rose a -> [Rose a] -> Tree a -- helper function given types
from2' (Rose a []) y = Node Tip a (from' y) -- Case 1: Rose a []
from2' (Rose a x) y = Node (from' x) a (from' y) -- Case 2: Rose a x (non-empty list)

to :: Rose a -> Fork a -- given function types
to (Rose a []) = Leaf a -- rule 1: simple rose-fork transmission
to (Rose a [Rose b []]) = Branch (Leaf b) (Leaf a) -- rule 2: 2-layer Rose a [] solution
to (Rose a [Rose b [], Rose c []]) = Branch (Leaf b) (Branch (Leaf c) (Leaf a)) -- rule 3: 2-layer composite solution
to (Rose a [x]) = Branch (to x) (Leaf a) -- Recursion of solving multi-layer problems (using pattern matching)

from :: Fork a -> Rose a -- given function types
from (Leaf a) = Rose a [] -- rule 1: simple fork-rose transformation
from (Branch (Leaf a) (Leaf b)) = Rose b [Rose a []] -- rule 2: simple branch transformation
from (Branch (Leaf a) (Branch (Leaf b) (Leaf c))) = Rose c [Rose a [], Rose b []] -- rule 3: copmposite branch transformation
from (Branch x (Leaf a)) = Rose a [from x] -- Recursion of solving multi-layer problems (using pattern matching)
\end{code}