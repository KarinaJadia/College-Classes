#include <iostream>
#include <vector>
#include "ECMatrix.h"



//implement all of the constructors and functions here

template<typename T>
Matrix<T> :: Matrix(size_t r, size_t c) : rows(r), cols(c), data(r, std::vector<T>(c, 0)) {}

template<typename T>
Matrix<T> :: Matrix(const Matrix& og) : rows(og.rows), cols(og.cols), data(og.data) {}

// operator overloads
// Make sure you check for undefined operations with matrix dimensions! Return [0] (1x1 matrix) if illegal. 

//equality == -> check each cell for equality

template<typename T>
bool Matrix<T>::operator==(const Matrix& m) const {
    if (rows != m.rows || cols != m.cols) return false;

    for (size_t i = 0; i < rows; ++i) {
        const auto& rowA = data[i];
        const auto& rowB = m.data[i];
        for (size_t j = 0; j < cols; ++j) {
            if (rowA[j] != rowB[j]) return false;
        }
    }

    return true;
}

// + -> add each cell to corresponding cell of the next matrix

template<typename T>
Matrix<T> Matrix<T>::operator+(const Matrix& m) const {
    if (rows != m.rows || cols != m.cols) return Matrix<T>(1, 1);

    Matrix<T> res(rows, cols);
    for (size_t i = 0; i < rows; ++i) {
        auto& row_res = res.data[i];
        const auto& row_a = data[i];
        const auto& row_b = m.data[i];
        for (size_t j = 0; j < cols; ++j) {
            row_res[j] = row_a[j] + row_b[j];
        }
    }

    return res;
}

// - -> //subtract each cell

template<typename T>
Matrix<T> Matrix<T>::operator-(const Matrix& m) const {
    if (rows != m.rows || cols != m.cols) return Matrix<T>(1, 1);

    Matrix<T> res(rows, cols);
    for (auto i = 0u; i < rows; ++i) {
        auto& res_row = res.data[i];
        const auto& row_a = data[i];
        const auto& row_b = m.data[i];

        for (auto col_idx = 0u; col_idx < cols; ++col_idx) {
            res_row[col_idx] = row_a[col_idx] - row_b[col_idx];
        }
    }

    return res;
}

// * -> matrix multiplication

template<typename T>
Matrix<T> Matrix<T>::operator*(const Matrix& m) const {
    if (cols != m.rows) return Matrix<T>(1, 1);

    Matrix<T> res(rows, m.cols);
    for (auto i = 0u; i < rows; ++i) {
        auto& res_row = res.data[i];
        const auto& row_a = data[i];

        for (auto j = 0u; j < m.cols; ++j) {
            T sum = 0;
            for (auto k = 0u; k < cols; ++k) {
                sum += row_a[k] * m.data[k][j];
            }
            res_row[j] = sum;
        }
    }

    return res;
}

// () -> getter/setter

template<typename T>
T& Matrix<T>::operator()(size_t r, size_t c) {
    return data[r][c];
}

// () const -> read-only getter

template<typename T>
const T& Matrix<T>::operator()(size_t r, size_t c) const {
    return data[r][c];
}

//other utility functions
//transpose() -> "rotate" matrix

template<typename T>
Matrix<T> Matrix<T>::transpose() const {

    Matrix<T> res(cols, rows);
    for (auto i = 0u; i < rows; ++i) {
        const auto& row = data[i];
        for (auto j = 0u; j < cols; ++j) {
            res.data[j][i] = row[j];
        }
    }

    return res;
}

//get number of rows

template<typename T>
size_t Matrix<T>::getNumRows() {
    return rows;
}

//get number of cols

template<typename T>
size_t Matrix<T>::getNumCols() {
    return cols;
}

// display() -> print out matrix pretty

template<typename T>
void Matrix<T>::display() const {
    for (const auto& row : data) {
        for (const auto& val : row)
            std::cout << val << " ";
        std::cout << std::endl;
    }
}

template class Matrix<int>;
template class Matrix<double>;
template class Matrix<float>;