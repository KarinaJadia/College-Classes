#include<iostream>

// Follow the comments to fully implement the following matrix class!

template<typename T>
class Matrix{

    public:

        //constructors
        Matrix(size_t r, size_t c);
        Matrix(const Matrix& original); //make a deep copy of the matrix passed in!

        //operator overloads
        bool operator==(const Matrix& rhs) const; //check equality of all cells in 2 matrices, as well as size
        Matrix operator+(const Matrix& rhs) const;
        Matrix operator-(const Matrix& rhs) const;
        Matrix operator*(const Matrix& rhs) const; //do matrix multiplication/dot product if possible, or return matrix of all 0 if not.
        T& operator()(size_t r, size_t c); //use this as the getter/setter from a specific cell
        const T& operator()(size_t r, size_t c) const; //read-only access
        
        //other useful matrix functions
        Matrix transpose() const; //return a matrix which has been "rotated" so the rows of the original are the columns of the output
        size_t getNumRows(); //return number of rows
        size_t getNumCols(); //return number of cols
        void display() const; //print out the matrix pretty

    private:
        std::vector<std::vector<T>> data; //2D vector representation
        const size_t rows;
        const size_t cols;

};
