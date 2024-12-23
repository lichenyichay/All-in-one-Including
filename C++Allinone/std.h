#pragma once
#ifndef STD_MODULE_H
#define STD_MODULE_H

// 基础输入输出流
#include <iostream>

// 字符串处理
#include <string>

// 向量容器
#include <vector>

// 算法支持
#include <algorithm>

// 数学函数
#include <cmath>
#include <complex>
using Complex = std::complex<double>;

// 内存管理
#include <memory>

// 容器适配器
#include <stack>
#include <queue>
#include <deque>

// 关联容器
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

// 迭代器支持
#include <iterator>

// 异常处理
#include <exception>

// 时间和日期
#include <chrono>
#include <ctime>

// 文件系统操作（C++17）
#if __cplusplus >= 201703L
#include <filesystem>
#endif

// 多线程支持（C++11）
#include <thread>
#include <mutex>
#include <future>
#include <condition_variable>

// 动态内存管理
#include <new>

// 类型特征
#include <type_traits>

// 函数对象
#include <functional>

// 随机数生成
#include <random>

// 正则表达式（C++11）
#include <regex>

// 数值限制
#include <limits>

// 格式化 I/O（C++20）
#if __cplusplus >= 202002L
#include <format>
#endif

//使用STD命名空间
using namespace std;

#endif // STD_MODULE_H
