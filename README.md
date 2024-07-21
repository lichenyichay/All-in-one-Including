# All-in-one Including

多功能一体机库版本，现已更新至4.0.0版本
说明如下：

```python
Help on module Allinone:

NAME
    Allinone

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/21 18:00
    # @FILE:Allinone.py
    # @version:4.0.0
    # @Software:Visual Studio Code

FUNCTIONS
    allinone(fuwu, mode, *args)
        :param fuwu 需要服务的功能
        :param mode 部分功能需要的模式（详见Github中All-in-one2.4.0分支的Wiki页）
        :param *args 可变参数，表示需要传入的参数，建议用元组或列表类型，具体所需类型见README.MD
        :return: 0：正常，1：不正常，其他返回值表示功能的结果

        功能（按代码顺序排序，不分先后）：大小写互换、抽取随机数、求最小公倍数、求最大公倍数、图形计算器、小学学生信息管理系统、二分查找、求余、向下取整、向上取整、多个数求和、多个数求差、多个数求积、判断闰年、判断是否为质数、整数、小数计算（加减乘除）、分数计算（加减乘除）......（具体见Github All-in-one2.4.0分支Readme.md文件）

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\allinone.py

Help on module xiaogongju:

NAME
    xiaogongju

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/21 17:20
    # @FILE:xiaogongju.py
    # @Software:IDLE 3.9.6

FUNCTIONS
    chouqusuiji(num1: int, num2: int, mode: int, weishu: int) -> str

    daorxiao(args: str, mode: int) -> str

    f(a: float, n: int, m: int) -> int

    kaisamima(arg: str, mode: int, n: int) -> str

    quzheng(num: float, mode: int) -> int

    twonumbers_TheBiggestCommonfactor(num1: int, num2: int) -> int

    twonumbers_TheMinimumCommonmultiple(num1: int, num2: int) -> int

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\xiaogongju.py

Help on module calculator:

NAME
    calculator

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/21 17:20
    # @FILE:calculator.py
    # @Software:Visual Studio Code

FUNCTIONS
    FtemporCtemp(mode: str, FtemporCtemp: float) -> float

    csqrt = sqrt(z, /)
        Return the square root of z.

    duihuan(mode: int, money: float) -> float

    fab(x: int) -> int

    factorization(num: int) -> list[int]

    fanzhuanzifuchuan(s: str) -> str

    fenjisuan(num1: str, num2: str, mode: str) -> float

    isfab(x: int) -> bool

    isfabhuiwenshu(x: int) -> bool

    isfabhuiwenzhishu(x: int) -> bool

    isfabparam(x: int) -> bool

    isfabwanquanpingfangshu(num: int) -> bool

    ishuiwenshu(d: int) -> bool

    ishuiwenzhishu(d: int) -> bool

    isleapyear(x) -> bool

    isparam(d: int) -> bool

    istribonacci(n: int) -> bool

    istribonaccihuiwenshu(n: int) -> bool

    istribonaccihuiwenshuparam(n: int) -> bool

    istribonacciparam(n: int) -> bool

    istribonacciwanquanpingfangshu(num: int) -> bool

    iswanquanpingfangshu(num: int) -> bool

    jinzhizhuanhuan(a: int, b: int, c: str) -> str

    mima(num: int, n: int) -> int

    tribonacci(n: int) -> int

    wanquanpingfangshu(num: int) -> int

    xiaoorfen(num: str, mode: int) -> str

    xiaoorzhengjisuan(num1: float, num2: float, mode: str) -> float

    yiyuannci(fangcheng: str, mode: int) -> tuple

DATA
    CC = CC
    Catalan = Catalan
    Complexes = Complexes
    E = E
    EX = EX
    EXRAW = EXRAW
    EmptySequence = EmptySequence
    EmptySet = EmptySet
    EulerGamma = EulerGamma
    FU = {'L': <function L>, 'TR0': <function TR0>, 'TR1': <function TR1>,...
    GoldenRatio = GoldenRatio
    I = I
    Id = Lambda(_x, _x)
    Integers = Integers
    Naturals = Naturals
    Naturals0 = Naturals0
    Q = <sympy.assumptions.ask.AssumptionKeys object>
    QQ = QQ
    QQ_I = QQ_I
    RR = RR
    Rationals = Rationals
    Reals = Reals
    S = S
    TribonacciConstant = TribonacciConstant
    UniversalSet = UniversalSet
    ZZ = ZZ
    ZZ_I = ZZ_I
    doctest = <LazyFunction object at 0x1aca0ce1ad0>: wrapping 'sympy.test...
            Runs doctests in all \*.py files in the SymPy directory which match
            any of the given strings in ``paths`` or all tests if paths=[].

            Notes:

            - Paths can be entered in native system format or in unix,
              forward-slash format.
            - Files that are on the blacklist can be tested by providing
              their path; they are only excluded if no paths are given.

            Examples
            ========

            >>> import sympy

            Run all tests:

            >>> sympy.doctest() # doctest: +SKIP

            Run one file:

            >>> sympy.doctest("sympy/core/basic.py") # doctest: +SKIP
            >>> sympy.doctest("polynomial.rst") # doctest: +SKIP

            Run all tests in sympy/functions/ and some particular file:

            >>> sympy.doctest("/functions", "basic.py") # doctest: +SKIP

            Run any file having polynomial in its name, doc/src/modules/polynomial.rst,
            sympy/functions/special/polynomials.py, and sympy/polys/polynomial.py:

            >>> sympy.doctest("polynomial") # doctest: +SKIP

            The ``split`` option can be passed to split the test run into parts. The
            split currently only splits the test files, though this may change in the
            future. ``split`` should be a string of the form 'a/b', which will run
            part ``a`` of ``b``. Note that the regular doctests and the Sphinx
            doctests are split independently. For instance, to run the first half of
            the test suite:

            >>> sympy.doctest(split='1/2')  # doctest: +SKIP

            The ``subprocess`` and ``verbose`` options are the same as with the function
            ``test()`` (see the docstring of that function for more information) except
            that ``verbose`` may also be set equal to ``2`` in order to print
            individual doctest lines, as they are being tested.


        Note: this is a LazyFunction wrapper of 'sympy.testing.runtests.doctest'

    false = False
    grevlex = ReversedGradedLexOrder()
    grlex = GradedLexOrder()
    igrevlex = InverseOrder()
    igrlex = InverseOrder()
    ilex = InverseOrder()
    latex = <sympy.printing.printer._PrintFunction object>
        Convert the given expression to LaTeX string representation.

        Parameters
        ==========
        full_prec: boolean, optional
            If set to True, a floating point number is printed with full precision.
        fold_frac_powers : boolean, optional
            Emit ``^{p/q}`` instead of ``^{\frac{p}{q}}`` for fractional powers.
        fold_func_brackets : boolean, optional
            Fold function brackets where applicable.
        fold_short_frac : boolean, optional
            Emit ``p / q`` instead of ``\frac{p}{q}`` when the denominator is
            simple enough (at most two terms and no powers). The default value is
            ``True`` for inline mode, ``False`` otherwise.
        inv_trig_style : string, optional
            How inverse trig functions should be displayed. Can be one of
            ``'abbreviated'``, ``'full'``, or ``'power'``. Defaults to
            ``'abbreviated'``.
        itex : boolean, optional
            Specifies if itex-specific syntax is used, including emitting
            ``$$...$$``.
        ln_notation : boolean, optional
            If set to ``True``, ``\ln`` is used instead of default ``\log``.
        long_frac_ratio : float or None, optional
            The allowed ratio of the width of the numerator to the width of the
            denominator before the printer breaks off long fractions. If ``None``
            (the default value), long fractions are not broken up.
        mat_delim : string, optional
            The delimiter to wrap around matrices. Can be one of ``'['``, ``'('``,
            or the empty string ``''``. Defaults to ``'['``.
        mat_str : string, optional
            Which matrix environment string to emit. ``'smallmatrix'``,
            ``'matrix'``, ``'array'``, etc. Defaults to ``'smallmatrix'`` for
            inline mode, ``'matrix'`` for matrices of no more than 10 columns, and
            ``'array'`` otherwise.
        mode: string, optional
            Specifies how the generated code will be delimited. ``mode`` can be one
            of ``'plain'``, ``'inline'``, ``'equation'`` or ``'equation*'``.  If
            ``mode`` is set to ``'plain'``, then the resulting code will not be
            delimited at all (this is the default). If ``mode`` is set to
            ``'inline'`` then inline LaTeX ``$...$`` will be used. If ``mode`` is
            set to ``'equation'`` or ``'equation*'``, the resulting code will be
            enclosed in the ``equation`` or ``equation*`` environment (remember to
            import ``amsmath`` for ``equation*``), unless the ``itex`` option is
            set. In the latter case, the ``$$...$$`` syntax is used.
        mul_symbol : string or None, optional
            The symbol to use for multiplication. Can be one of ``None``,
            ``'ldot'``, ``'dot'``, or ``'times'``.
        order: string, optional
            Any of the supported monomial orderings (currently ``'lex'``,
            ``'grlex'``, or ``'grevlex'``), ``'old'``, and ``'none'``. This
            parameter does nothing for `~.Mul` objects. Setting order to ``'old'``
            uses the compatibility ordering for ``~.Add`` defined in Printer. For
            very large expressions, set the ``order`` keyword to ``'none'`` if
            speed is a concern.
        symbol_names : dictionary of strings mapped to symbols, optional
            Dictionary of symbols and the custom strings they should be emitted as.
        root_notation : boolean, optional
            If set to ``False``, exponents of the form 1/n are printed in fractonal
            form. Default is ``True``, to print exponent in root form.
        mat_symbol_style : string, optional
            Can be either ``'plain'`` (default) or ``'bold'``. If set to
            ``'bold'``, a `~.MatrixSymbol` A will be printed as ``\mathbf{A}``,
            otherwise as ``A``.
        imaginary_unit : string, optional
            String to use for the imaginary unit. Defined options are ``'i'``
            (default) and ``'j'``. Adding ``r`` or ``t`` in front gives ``\mathrm``
            or ``\text``, so ``'ri'`` leads to ``\mathrm{i}`` which gives
            `\mathrm{i}`.
        gothic_re_im : boolean, optional
            If set to ``True``, `\Re` and `\Im` is used for ``re`` and ``im``, respectively.
            The default is ``False`` leading to `\operatorname{re}` and `\operatorname{im}`.
        decimal_separator : string, optional
            Specifies what separator to use to separate the whole and fractional parts of a
            floating point number as in `2.5` for the default, ``period`` or `2{,}5`
            when ``comma`` is specified. Lists, sets, and tuple are printed with semicolon
            separating the elements when ``comma`` is chosen. For example, [1; 2; 3] when
            ``comma`` is chosen and [1,2,3] for when ``period`` is chosen.
        parenthesize_super : boolean, optional
            If set to ``False``, superscripted expressions will not be parenthesized when
            powered. Default is ``True``, which parenthesizes the expression when powered.
        min: Integer or None, optional
            Sets the lower bound for the exponent to print floating point numbers in
            fixed-point format.
        max: Integer or None, optional
            Sets the upper bound for the exponent to print floating point numbers in
            fixed-point format.
        diff_operator: string, optional
            String to use for differential operator. Default is ``'d'``, to print in italic
            form. ``'rd'``, ``'td'`` are shortcuts for ``\mathrm{d}`` and ``\text{d}``.
        adjoint_style: string, optional
            String to use for the adjoint symbol. Defined options are ``'dagger'``
            (default),``'star'``, and ``'hermitian'``.

        Notes
        =====

        Not using a print statement for printing, results in double backslashes for
        latex commands since that's the way Python escapes backslashes in strings.

        >>> from sympy import latex, Rational
        >>> from sympy.abc import tau
        >>> latex((2*tau)**Rational(7,2))
        '8 \\sqrt{2} \\tau^{\\frac{7}{2}}'
        >>> print(latex((2*tau)**Rational(7,2)))
        8 \sqrt{2} \tau^{\frac{7}{2}}

        Examples
        ========

        >>> from sympy import latex, pi, sin, asin, Integral, Matrix, Rational, log
        >>> from sympy.abc import x, y, mu, r, tau

        Basic usage:

        >>> print(latex((2*tau)**Rational(7,2)))
        8 \sqrt{2} \tau^{\frac{7}{2}}

        ``mode`` and ``itex`` options:

        >>> print(latex((2*mu)**Rational(7,2), mode='plain'))
        8 \sqrt{2} \mu^{\frac{7}{2}}
        >>> print(latex((2*tau)**Rational(7,2), mode='inline'))
        $8 \sqrt{2} \tau^{7 / 2}$
        >>> print(latex((2*mu)**Rational(7,2), mode='equation*'))
        \begin{equation*}8 \sqrt{2} \mu^{\frac{7}{2}}\end{equation*}
        >>> print(latex((2*mu)**Rational(7,2), mode='equation'))
        \begin{equation}8 \sqrt{2} \mu^{\frac{7}{2}}\end{equation}
        >>> print(latex((2*mu)**Rational(7,2), mode='equation', itex=True))
        $$8 \sqrt{2} \mu^{\frac{7}{2}}$$
        >>> print(latex((2*mu)**Rational(7,2), mode='plain'))
        8 \sqrt{2} \mu^{\frac{7}{2}}
        >>> print(latex((2*tau)**Rational(7,2), mode='inline'))
        $8 \sqrt{2} \tau^{7 / 2}$
        >>> print(latex((2*mu)**Rational(7,2), mode='equation*'))
        \begin{equation*}8 \sqrt{2} \mu^{\frac{7}{2}}\end{equation*}
        >>> print(latex((2*mu)**Rational(7,2), mode='equation'))
        \begin{equation}8 \sqrt{2} \mu^{\frac{7}{2}}\end{equation}
        >>> print(latex((2*mu)**Rational(7,2), mode='equation', itex=True))
        $$8 \sqrt{2} \mu^{\frac{7}{2}}$$

        Fraction options:

        >>> print(latex((2*tau)**Rational(7,2), fold_frac_powers=True))
        8 \sqrt{2} \tau^{7/2}
        >>> print(latex((2*tau)**sin(Rational(7,2))))
        \left(2 \tau\right)^{\sin{\left(\frac{7}{2} \right)}}
        >>> print(latex((2*tau)**sin(Rational(7,2)), fold_func_brackets=True))
        \left(2 \tau\right)^{\sin {\frac{7}{2}}}
        >>> print(latex(3*x**2/y))
        \frac{3 x^{2}}{y}
        >>> print(latex(3*x**2/y, fold_short_frac=True))
        3 x^{2} / y
        >>> print(latex(Integral(r, r)/2/pi, long_frac_ratio=2))
        \frac{\int r\, dr}{2 \pi}
        >>> print(latex(Integral(r, r)/2/pi, long_frac_ratio=0))
        \frac{1}{2 \pi} \int r\, dr

        Multiplication options:

        >>> print(latex((2*tau)**sin(Rational(7,2)), mul_symbol="times"))
        \left(2 \times \tau\right)^{\sin{\left(\frac{7}{2} \right)}}

        Trig options:

        >>> print(latex(asin(Rational(7,2))))
        \operatorname{asin}{\left(\frac{7}{2} \right)}
        >>> print(latex(asin(Rational(7,2)), inv_trig_style="full"))
        \arcsin{\left(\frac{7}{2} \right)}
        >>> print(latex(asin(Rational(7,2)), inv_trig_style="power"))
        \sin^{-1}{\left(\frac{7}{2} \right)}

        Matrix options:

        >>> print(latex(Matrix(2, 1, [x, y])))
        \left[\begin{matrix}x\\y\end{matrix}\right]
        >>> print(latex(Matrix(2, 1, [x, y]), mat_str = "array"))
        \left[\begin{array}{c}x\\y\end{array}\right]
        >>> print(latex(Matrix(2, 1, [x, y]), mat_delim="("))
        \left(\begin{matrix}x\\y\end{matrix}\right)

        Custom printing of symbols:

        >>> print(latex(x**2, symbol_names={x: 'x_i'}))
        x_i^{2}

        Logarithms:

        >>> print(latex(log(10)))
        \log{\left(10 \right)}
        >>> print(latex(log(10), ln_notation=True))
        \ln{\left(10 \right)}

        ``latex()`` also supports the builtin container types :class:`list`,
        :class:`tuple`, and :class:`dict`:

        >>> print(latex([2/x, y], mode='inline'))
        $\left[ 2 / x, \  y\right]$

        Unsupported types are rendered as monospaced plaintext:

        >>> print(latex(int))
        \mathtt{\text{<class 'int'>}}
        >>> print(latex("plain % text"))
        \mathtt{\text{plain \% text}}

        See :ref:`printer_method_example` for an example of how to override
        this behavior for your own types by implementing ``_latex``.

        .. versionchanged:: 1.7.0
            Unsupported types no longer have their ``str`` representation treated as valid latex.

    lex = LexOrder()
    mathml = <sympy.printing.printer._PrintFunction object>
        Returns the MathML representation of expr. If printer is presentation
        then prints Presentation MathML else prints content MathML.

    nan = nan
    oo = oo
    ord0 = ord0
    pi = pi
    plot_backends = {'matplotlib': <class 'sympy.plotting.backends.matplot...
    pretty = <sympy.printing.printer._PrintFunction object>
        Returns a string containing the prettified form of expr.

        For information on keyword arguments see pretty_print function.

    sieve = <prime sieve (6): 2, 3, 5, ... 11, 13
    totient si..., ... 2, 4
    ...
    srepr = <sympy.printing.printer._PrintFunction object>
        return expr in repr form

    sstr = <sympy.printing.printer._PrintFunction object>
        Returns the expression as a string.

        For large expressions where speed is a concern, use the setting
        order='none'. If abbrev=True setting is used then units are printed in
        abbreviated form.

        Examples
        ========

        >>> from sympy import symbols, Eq, sstr
        >>> a, b = symbols('a b')
        >>> sstr(Eq(a + b, 0))
        'Eq(a + b, 0)'

    sstrrepr = <sympy.printing.printer._PrintFunction object>
        return expr in mixed str/repr form

        i.e. strings are returned in repr form with quotes, and everything else
        is returned in str form.

        This function could be useful for hooking into sys.displayhook

    test = <LazyFunction object at 0x1ac9fcb9cd0>: wrapping 'sympy.testing...
        Interface to run tests via pytest compatible with SymPy's test runner.

            Explanation
            ===========

            Note that a `pytest.ExitCode`, which is an `enum`, is returned. This is
            different to the legacy SymPy test runner which would return a `bool`. If
            all tests sucessfully pass the `pytest.ExitCode.OK` with value `0` is
            returned, whereas the legacy SymPy test runner would return `True`. In any
            other scenario, a non-zero `enum` value is returned, whereas the legacy
            SymPy test runner would return `False`. Users need to, therefore, be careful
            if treating the pytest exit codes as booleans because
            `bool(pytest.ExitCode.OK)` evaluates to `False`, the opposite of legacy
            behaviour.

            Examples
            ========

            >>> import sympy  # doctest: +SKIP

            Run one file:

            >>> sympy.test('sympy/core/tests/test_basic.py')  # doctest: +SKIP
            >>> sympy.test('_basic')  # doctest: +SKIP

            Run all tests in sympy/functions/ and some particular file:

            >>> sympy.test("sympy/core/tests/test_basic.py",
            ...            "sympy/functions")  # doctest: +SKIP

            Run all tests in sympy/core and sympy/utilities:

            >>> sympy.test("/core", "/util")  # doctest: +SKIP

            Run specific test from a file:

            >>> sympy.test("sympy/core/tests/test_basic.py",
            ...            kw="test_equality")  # doctest: +SKIP

            Run specific test from any file:

            >>> sympy.test(kw="subs")  # doctest: +SKIP

            Run the tests using the legacy SymPy runner:

            >>> sympy.test(use_sympy_runner=True)  # doctest: +SKIP

            Note that this option is slated for deprecation in the near future and is
            only currently provided to ensure users have an alternative option while the
            pytest-based runner receives real-world testing.

            Parameters
            ==========
            paths : first n positional arguments of strings
                Paths, both partial and absolute, describing which subset(s) of the test
                suite are to be run.
            subprocess : bool, default is True
                Legacy option, is currently ignored.
            rerun : int, default is 0
                Legacy option, is ignored.
            use_sympy_runner : bool or None, default is None
                Temporary option to invoke the legacy SymPy test runner instead of
                `pytest.main`. Will be removed in the near future.
            verbose : bool, default is False
                Sets the verbosity of the pytest output. Using `True` will add the
                `--verbose` option to the pytest call.
            tb : str, 'auto', 'long', 'short', 'line', 'native', or 'no'
                Sets the traceback print mode of pytest using the `--tb` option.
            kw : str
                Only run tests which match the given substring expression. An expression
                is a Python evaluatable expression where all names are substring-matched
                against test names and their parent classes. Example: -k 'test_method or
                test_other' matches all test functions and classes whose name contains
                'test_method' or 'test_other', while -k 'not test_method' matches those
                that don't contain 'test_method' in their names. -k 'not test_method and
                not test_other' will eliminate the matches. Additionally keywords are
                matched to classes and functions containing extra names in their
                'extra_keyword_matches' set, as well as functions which have names
                assigned directly to them. The matching is case-insensitive.
            pdb : bool, default is False
                Start the interactive Python debugger on errors or `KeyboardInterrupt`.
            colors : bool, default is True
                Color terminal output.
            force_colors : bool, default is False
                Legacy option, is ignored.
            sort : bool, default is True
                Run the tests in sorted order. pytest uses a sorted test order by
                default. Requires pytest-randomly.
            seed : int
                Seed to use for random number generation. Requires pytest-randomly.
            timeout : int, default is 0
                Timeout in seconds before dumping the stacks. 0 means no timeout.
                Requires pytest-timeout.
            fail_on_timeout : bool, default is False
                Legacy option, is currently ignored.
            slow : bool, default is False
                Run the subset of tests marked as `slow`.
            enhance_asserts : bool, default is False
                Legacy option, is currently ignored.
            split : string in form `<SPLIT>/<GROUPS>` or None, default is None
                Used to split the tests up. As an example, if `split='2/3' is used then
                only the middle third of tests are run. Requires pytest-split.
            time_balance : bool, default is True
                Legacy option, is currently ignored.
            blacklist : iterable of test paths as strings, default is BLACKLIST_DEFAULT
                Blacklisted test paths are ignored using the `--ignore` option. Paths
                may be partial or absolute. If partial then they are matched against
                all paths in the pytest tests path.
            parallel : bool, default is False
                Parallelize the test running using pytest-xdist. If `True` then pytest
                will automatically detect the number of CPU cores available and use them
                all. Requires pytest-xdist.
            store_durations : bool, False
                Store test durations into the file `.test_durations`. The is used by
                `pytest-split` to help determine more even splits when more than one
                test group is being used. Requires pytest-split.



        Note: this is a LazyFunction wrapper of 'sympy.testing.runtests_pytest.test'

    true = True
    zoo = zoo

VERSION
    1.13.1

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\calculator.py

Help on module numbertochinese:

NAME
    numbertochinese

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/07/21 18:00
    # @FILE:numbertochinese.py
    # @version:4.0.0
    # @Software:Visual Studio Code

FUNCTIONS
    No2Cn(number: int) -> str

    chinese2digits(uchars_chinese)

    maxdigit(number: int, count: int) -> tuple

DATA
    common_used_numerals = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '日': 7, '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
    digitdict = {1: '十', 2: '百', 3: '千', 4: '万'}
    numdict = {1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",0:"零"}

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\numbertochinese.py

Help on module lotterytickets:

NAME
    lotterytickets

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2024/5/3 23:25
    # @FILE:lotterytickets.py
    # @version:4.0.0
    # @Software:Visual Studio Code

FUNCTIONS
    lotterytickets(user: str, mubiao: str, mode: int) -> str

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\lotterytickets.py


Help on module erfenchazhao_py:

NAME
    erfenchazhao_py

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2022/12/25 9:03
    # @FILE:erfenchazhao_py.py
    # @Software:IDLE 3.9.6

FUNCTIONS
    erfenchazhao(yuanlst, shengxulst, target)

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\erfenchazhao_py.py


Help on module math_cal_py:

NAME
    math_cal_py

DESCRIPTION
    # -*- coding:UTF-8 -*-
    # @Author:Chay
    # @TIME:2022/12/24 15:38
    # @FILE:math_cal_py.py
    # @Software:IDLE 3.9.6

FUNCTIONS
    math_cal(mode, float1, float2)

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\math_cal_py.py


Help on module student_py:

NAME
    student_py

DESCRIPTION
    函数名：student
    调用形式：student()
    作用：小学学生信息管理系统

FUNCTIONS
    student()

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\student_py.py


Help on module tuxing_cal:

NAME
    tuxing_cal

DESCRIPTION
    函数名：tuxing
    调用形式：tuxing(huida)
    :param huida 图形
    :return 0
    作用：进行图形计算

FUNCTIONS
    tuxing(huida, mode, *args2)

FILE
    d:\chay\project\all-in-one\src\all-in-one_chaylichenyi\module\tuxing_cal.py



```

详见<https://github.com/lichenyichay/All-in-one>
