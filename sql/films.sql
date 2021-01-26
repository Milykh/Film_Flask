-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Янв 26 2021 г., 02:31
-- Версия сервера: 10.3.22-MariaDB
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `films`
--

-- --------------------------------------------------------

--
-- Структура таблицы `film`
--

CREATE TABLE `film` (
  `id_film` int(11) NOT NULL,
  `name_film` varchar(50) NOT NULL,
  `descript_film` text NOT NULL,
  `year_film` year(4) NOT NULL,
  `country` varchar(50) NOT NULL,
  `producer` varchar(50) NOT NULL,
  `s_writer` varchar(50) NOT NULL,
  `actors` varchar(250) NOT NULL,
  `duration` int(10) NOT NULL,
  `poster_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `film`
--

INSERT INTO `film` (`id_film`, `name_film`, `descript_film`, `year_film`, `country`, `producer`, `s_writer`, `actors`, `duration`, `poster_id`) VALUES
(40, 'Ла-Ла Ленд', 'Миа всегда знала, чего она хочет: девушка мечтала однажды проснуться знаменитой голливудской актрисой. Ради этого главная героиня постоянно ходила на кастинги, но ни один режиссер ее не замечал. Тогда девушка решила устроиться в один очень престижный ресторан, который посещают известные актеры и режиссеры. Миа надеялась, что когда-то все-таки ее заметят. Когда девушка в очередной раз пришла на работу, то стала', 2016, 'США', 'Дэмьен Шазелл', 'Дэмьен Шазелл', 'Райан Гослинг, Эмма Стоун, ', 122, 43),
(41, 'На острие', 'Знаменитая саблистка Александра побеждает всегда и везде. Она участвует во множестве соревнований, и знает, что ей нет равных. К своей славе она шла очень долго, путь был тернистым, но сейчас она добилась своего и рада этому. Ей осталось сделать только один момент, у нее нет', 2020, 'На острие', 'Эдуард Бордуков', 'Эдуард Бордуков', 'Светлана Ходченкова, Стася Милославская, Сергей Пускепалис, Алексей Барабаш, Евгений Сытый,', 122, 44),
(50, 'На острие', 'Знаменитая саблистка Александра побеждает всегда и везде. Она участвует во множестве соревнований, и знает, что ей нет равных. К своей славе она шла очень долго, путь был тернистым, но сейчас она добилась своего и рада этому. Ей осталось сделать только один момент, у нее нет олимпийской медали, и она стремится к этому.', 2020, ' Россия', 'Эдуард Бордуков', 'Эдуард Бордуков', 'Светлана Ходченкова, Стася Милославская', 111, 44),
(51, 'Breaking Surface', 'Ида и Тува сводные сестры, которые сумели подружиться между собой и найти общий язык. Молодые девушки имеют много общих интересов, они всегда проводили время вместе. Также стоит отметить тот факт, что каждый год девушки едут на территорию северной Норвегии, для того чтобы заниматься зимним дайвингом', 2020, ' Швеция, Норвегия, Бельгия', ' Йоахим Хеден', ' Йоахим Хеден', 'Муа Гаммель, Мадлен Мартин, Трине Вигген', 81, 55),
(52, 'Под откос', 'В жизни любой семьи происходят кризисы, особенно если люди живут вместе уже много лет, у них дети уже стали взрослыми, и в недавнем времени у одного из родителей умерла мама', 2021, 'США', 'Нат Факсон, Джим Рэш', 'Нат Факсон, Джим Рэш', 'Джулия Луис-Дрейфус, Уилл Феррелл, Миранда Отто, Зои Чао,', 86, 56),
(53, 'Огонек-Огниво', ' Сюжет фильма знакомит с такими понятиями как вера и любовь, внимание и преданность. Но даже помимо таких качеств человека, здесь будут фигурировать и такие как жадность, злоба и зависть.', 2021, 'Россия', 'Константин Щекин', 'Константин Щекин', ' Наталья Терешкова, Эдгард Запашный, Пётр Коврижных,', 77, 57),
(54, 'Гретель и Гензель', 'Увлеченности современными телефонами и новейшими гаджетами приводит все современное человечество к деградации. Люди меньше обращают внимание на проблемы и разные события, происходящие вокруг них. Они тут же забывают о своей личной жизни и понятия не имели прелести живого общения.', 2020, ' Канада, Ирландия, США, ЮАР', 'Оз Перкинс', ' София Лиллис, ', ' София Лиллис, Сэмми Лики, Элис Крайдж, Джессика Де Гау,', 88, 58),
(55, ' Пещера', 'Амани молодая и привлекательная девушка, которая живет на территории Сирии. Девушка работает в местной больнице доктором. Девушка вместе с другими профессиональными докторами оказывала медицинскую помощь раненым людям, которые оказались в опасных ситуациях', 2019, ' Таиланд, Ирландия', 'Том Уоллер', 'Том Уоллер', ' Рон Смуренбург, Мэйтави Уайсс, Лоуренс де Стефано, Келли', 104, 59),
(56, 'Видоизменённый углерод: Восстановленный', 'События происходят в будущем, когда все человечество успело достичь невероятных вершин технического прогресса. Отныне сознание можно было бы сохранить, если все перенести на специальный носитель. ', 2020, 'Япония, США', 'Такэру Накадзима, Ёсиюки Окада', 'Такэру Накадзима, Ёсиюки Окада', ' Тацухиса Судзуки, Рина Сато, Аяка Асаи, Дзёдзи Наката,', 74, 60),
(57, ' Вызов', ' Молодой парень Джей, жил вполне тихой и нормальной жизнью, у него рядом была любимая семья. Главный герой длительное время работал на такой работе, где практически не было выходных, именно по этой причине его супруга', 2019, ' Болгария, США, Великобритания', ' Джиллз Алдерсон', ' Джиллз Алдерсон', 'Виктория Ананьева, Перселл Аскотт, Alexander Biehn, Ричард', 88, 61),
(58, ' Котел', 'Савелий молодой и привлекательный парень, который жил тихой и размеренной жизнью. Длительное время он был хозяином компьютерного клуба, который назывался Котел, и при этом Савелий был доволен своей жизнью', 2020, 'Россия', 'Ева Басс', 'Ева Басс', 'Александр Кузнецов, Александра Ревенко, Василий Буткевич,', 888, 62);

-- --------------------------------------------------------

--
-- Структура таблицы `film_genre`
--

CREATE TABLE `film_genre` (
  `film_id` int(11) NOT NULL,
  `g_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `film_genre`
--

INSERT INTO `film_genre` (`film_id`, `g_id`) VALUES
(41, 3),
(50, 6),
(51, 8),
(52, 4),
(53, 1),
(54, 9),
(55, 6),
(56, 2),
(57, 2),
(58, 6);

-- --------------------------------------------------------

--
-- Структура таблицы `film_gl`
--

CREATE TABLE `film_gl` (
  `id_page` int(11) NOT NULL,
  `name_film` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name_g` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `year_film` year(4) NOT NULL,
  `count_rev` int(50) DEFAULT NULL,
  `id_film` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `film_gl`
--

INSERT INTO `film_gl` (`id_page`, `name_film`, `name_g`, `year_film`, `count_rev`, `id_film`) VALUES
(1, 'Под откос', 'комедия', 2021, 0, 52),
(2, 'Огонек-Огниво', 'боевик', 2021, 0, 53),
(3, 'Видоизменённый углерод: Восстановленный', 'детектив', 2020, 0, 56),
(4, 'На острие', 'исторический', 2020, 0, 41),
(5, 'Гретель и Гензель', 'ужасы', 2020, 0, 54),
(6, ' Котел', 'мелодрама', 2020, 1, 58),
(7, 'Breaking Surface', 'триллер', 2020, 0, 51),
(8, ' Вызов', 'детектив', 2019, 1, 57),
(9, ' Пещера', 'мелодрама', 2019, 0, 55),
(10, 'Ла-Ла Ленд', NULL, 2016, 1, 40);

-- --------------------------------------------------------

--
-- Структура таблицы `genre`
--

CREATE TABLE `genre` (
  `id_g` int(11) NOT NULL,
  `name_g` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `genre`
--

INSERT INTO `genre` (`id_g`, `name_g`) VALUES
(1, 'боевик'),
(2, 'детектив'),
(3, 'исторический'),
(4, 'комедия'),
(5, 'катастрофа'),
(6, 'мелодрама'),
(7, 'музыкальный'),
(8, 'триллер'),
(9, 'ужасы'),
(10, 'фантастика');

-- --------------------------------------------------------

--
-- Структура таблицы `poster`
--

CREATE TABLE `poster` (
  `id_poster` int(11) NOT NULL,
  `name_file` varchar(50) NOT NULL,
  `MIME` varchar(50) NOT NULL,
  `MD5` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `poster`
--

INSERT INTO `poster` (`id_poster`, `name_file`, `MIME`, `MD5`) VALUES
(7, 'ssafd.jpg', 'file', '4756210292d148d43f8d3af3c155cc5b'),
(8, 'ewer.jpg', 'file', 'f789c84ef9f707a9126e92e128714976'),
(9, 'ddsd.jpg', 'file', '8af14b97ae1224bfcd430ce1685ca447'),
(10, '.jpg', 'file', '4756210292d148d43f8d3af3c155cc5b'),
(11, 'цууу.jpg', 'file', '4ab0273600337bfe260ecaee012a7269'),
(12, 'weerr.jpg', 'file', '1b24b3ef227662d5156f796d321206c7'),
(13, 'errrr.jpg', 'file', '30dd38dacc6ef7e931d2a2c18d037d1f'),
(14, 'dfdffd.jpg', 'file', 'be876a292e36c9165be0753f7b72f289'),
(15, 'dddddd.jpg', 'file', '8a0e19fde02d28d4d0b6e869498070e1'),
(16, 'eeeeeeeeeeeeee.jpg', 'file', '6ca5e0c4340508daa11443014ea1f1e6'),
(17, 'sdfdsf.jpg', 'file', '3044f3f5073ea62d61935506a6f70ea2'),
(18, '.jpg', 'file', 'd6dfd321e67c137033f412f6034e7056'),
(19, '.jpg', 'file', '9115481d279dd07332148a0f5c704abc'),
(20, 'lord-war-e1336654779942.jpg', 'file', '4ab0273600337bfe260ecaee012a7269'),
(21, 'sanctum.jpg', 'file', '1846b9ecb385208e95918943dfea568c'),
(22, 'GGGGGGGGGGGG.jpg', 'file', 'f789c84ef9f707a9126e92e128714976'),
(23, 'SEESS.jpg', 'file', '5a3cab16a9776379328aacb5397ba2be'),
(24, 'where-the-wild-things-are.jpg', 'file', '45f25008a3647f5a6e6da79706c5e79a'),
(25, 'dsaf.jpg', 'file', 'e69768926f7804f6c56a1bbc91229284'),
(26, 're.jpg', 'file', 'a10293f41daada4dda77e4d137b8d053'),
(27, 'dfdf.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(28, 'dsadfdfgsdxc.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(29, 'gfjhgj.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(30, 'wer.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(31, 'weeeeee.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(32, 'werr.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(33, 'dfg.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(34, 'dfff.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(35, 'ertt.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(36, 'fdgfd.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(37, 'sdfgs.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(38, 'dsa.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(39, 'weeeew.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(40, 'reerere.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(41, 'wesr.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(42, 'wsaewq.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(43, 'Ла-Ла Ленд.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(44, 'ffd9b4ea27.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(45, 'f73802ff29.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(46, '90b7de9f3c.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(47, 'd6004a0f8f.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(48, 'f10e2821bb.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(49, 'ab54d7a264.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(50, '84bdd41a9b.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(51, '8f7dda1920.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(52, '722c2b67cc.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(53, 'ffd9b4ea27.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(54, 'ffd9b4ea27.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(55, '02c80cc307.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(56, 'e46506d843.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(57, '9ef446f4b8.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(58, '8ab073cfe6.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(59, '2832514d54.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(60, 'b19937f0d8.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(61, '557d757e20.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e'),
(62, '7319907bb3.jpg', 'file', 'd41d8cd98f00b204e9800998ecf8427e');

-- --------------------------------------------------------

--
-- Структура таблицы `review`
--

CREATE TABLE `review` (
  `id_rev` int(11) NOT NULL,
  `film_id` int(11) NOT NULL,
  `userexam_id` int(11) NOT NULL,
  `mark` int(1) NOT NULL,
  `text_r` text DEFAULT NULL,
  `data_r` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `review`
--

INSERT INTO `review` (`id_rev`, `film_id`, `userexam_id`, `mark`, `text_r`, `data_r`) VALUES
(33, 40, 1, 5, 'Молодые девушки имеют много общих интересов, они всегда проводили время вместе. Также стоит отметить тот факт, что каждый год девушки едут на территорию северной Норвегии, для того чтобы заниматься зимним дайвингом. Девушки это делали не просто так, именно таким образом они почтили память своей покойной мамы. Очередное погружение родственниц начинается как всегда, кажется, что ничего не предвещает беды. Девушки начали наслаждаться красотой подводного мира. Внезапно со скалы в', '2021-01-24 22:42:37'),
(40, 58, 4, 4, ' Идеальная жизнь продолжалась до того момента, как парень не узнал о том, что его лучший друг покончил с собой. Се происходящие события Савелию казались довольно таки странными, ведь он был уверен в том, что его друг не мог пойти на такой отчаянный шаг самостоятельно. Савелий никак не может отойти от такого удара, он решает окончательно порвать со своей нынешней жизнью, бросить все и уехать как можно дальше с', '2021-01-25 19:46:30'),
(41, 57, 8, 3, 'Такой распорядок сильно напрягал девушку, вот только найти выход из сложившейся ситуации она так и не могла. Однажды, был простой и тихий день, у парня появляется свободный вечер, который он может провести со своей семьей, вот только почему-то в этот раз что-то пошло не по плану. Неизвестные преступники похищают Джея прямо из его дома, и бросают его в подвал, где сидели другие жертвы. Спустя некоторое время у ним в подвал спускается садист в маске и начинает над всеми жестоко издеваться. Пленникам показалось, что они уже не смогут спастись из этой ситуации, но им все равно хотелось знать', '2021-01-25 19:47:29');

-- --------------------------------------------------------

--
-- Структура таблицы `role`
--

CREATE TABLE `role` (
  `id_role` int(11) NOT NULL,
  `name_role` varchar(50) NOT NULL,
  `descript_role` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `role`
--

INSERT INTO `role` (`id_role`, `name_role`, `descript_role`) VALUES
(1, 'администратор', 'Суперпользователь\r\nДоступны все действия на сайте'),
(2, 'модератор', 'Просмотр и редактирование фильмов\r\nМодерация рецензий'),
(3, 'пользователь', 'Может оставлять рецензии');

-- --------------------------------------------------------

--
-- Структура таблицы `user_exam`
--

CREATE TABLE `user_exam` (
  `id_userexam` int(11) NOT NULL,
  `login` varchar(50) NOT NULL,
  `hash` varchar(250) NOT NULL,
  `s_name` varchar(50) NOT NULL,
  `f_name` varchar(50) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `user_exam`
--

INSERT INTO `user_exam` (`id_userexam`, `login`, `hash`, `s_name`, `f_name`, `role_id`) VALUES
(1, 'admin', 'pbkdf2:sha256:150000$1KrrqKiv$4a051eade6a35c9de7d57fce43cf7ca08492f4c6b07af5f2115d8d462db4de9f', 'admin', 'adm', 1),
(2, 'mod', 'pbkdf2:sha256:150000$ffQJyxOh$84d47cc796e7ca3506065b4d4321303f1af09e82d0408a071bff017c6893771d', 'модератор', 'модератор', 2),
(3, 'user', 'pbkdf2:sha256:150000$yfOve1Iy$383088906ee14b6a07113652b95a40ec326ad93e37fe31601881587ba2ee7178', 'пользователь', 'пользователь', 3),
(4, 'user2', 'pbkdf2:sha256:150000$XaSmNImU$c61b3d65bb6fd4c005ac33a5c7e9ba3329867b7ffc0b83f9bd2fb9c4ca0409cc', 'ilya', 'j', 3),
(5, 'user3', 'pbkdf2:sha256:150000$Trke5Oex$2ad5bb869c6a2eb5cc4d7b6f861f7e085a08cde383dd9dd3a89a5aa2f4a8bd2c', 'fill', 'g', 3),
(6, 'user4', 'pbkdf2:sha256:150000$ApyEKnhu$7b1a55e8d45f18de324dcca265a23ad07843f159f399a909f66f759647569506', 'ivan', 'b', 3),
(8, 'user5', 'pbkdf2:sha256:150000$NgNcMD12$cce8c1d40ad505a01cfa8e0d7d8bf04ca8cf7cbf7c05dae0162d63deaac1f3eb', 'g_ilya', 'j', 3),
(9, 'user6', 'pbkdf2:sha256:150000$Lfc1vWMB$6d2de118dd02d0c8f649f305d6ec21a2bd9c1c3c1c512e3cf461625392bfcff2', 'w_fill', 'g', 3),
(10, 'user7', 'pbkdf2:sha256:150000$LzYTzXmW$b36d5e1f1ffa2742d4b0356caac25045763b7a8b9115be61d57503a868ea7683', 's_ivan', 'b', 3),
(11, 'user8', 'pbkdf2:sha256:150000$JJqtRc84$9c0fdf4f1753174873e9e53c9b222ce4aa1f2cdbce437b14440e08daf8191727', 'f_petr', 'v', 3);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`id_film`),
  ADD KEY `poster_id` (`poster_id`);

--
-- Индексы таблицы `film_genre`
--
ALTER TABLE `film_genre`
  ADD PRIMARY KEY (`film_id`,`g_id`),
  ADD KEY `g_id` (`g_id`);

--
-- Индексы таблицы `film_gl`
--
ALTER TABLE `film_gl`
  ADD PRIMARY KEY (`id_page`);

--
-- Индексы таблицы `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`id_g`);

--
-- Индексы таблицы `poster`
--
ALTER TABLE `poster`
  ADD PRIMARY KEY (`id_poster`);

--
-- Индексы таблицы `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`id_rev`),
  ADD KEY `film_id` (`film_id`),
  ADD KEY `userexam_id` (`userexam_id`);

--
-- Индексы таблицы `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id_role`);

--
-- Индексы таблицы `user_exam`
--
ALTER TABLE `user_exam`
  ADD PRIMARY KEY (`id_userexam`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `film`
--
ALTER TABLE `film`
  MODIFY `id_film` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT для таблицы `film_gl`
--
ALTER TABLE `film_gl`
  MODIFY `id_page` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `genre`
--
ALTER TABLE `genre`
  MODIFY `id_g` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `poster`
--
ALTER TABLE `poster`
  MODIFY `id_poster` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT для таблицы `review`
--
ALTER TABLE `review`
  MODIFY `id_rev` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT для таблицы `role`
--
ALTER TABLE `role`
  MODIFY `id_role` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `user_exam`
--
ALTER TABLE `user_exam`
  MODIFY `id_userexam` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `film`
--
ALTER TABLE `film`
  ADD CONSTRAINT `film_ibfk_1` FOREIGN KEY (`poster_id`) REFERENCES `poster` (`id_poster`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `film_genre`
--
ALTER TABLE `film_genre`
  ADD CONSTRAINT `film_genre_ibfk_1` FOREIGN KEY (`film_id`) REFERENCES `film` (`id_film`) ON DELETE CASCADE,
  ADD CONSTRAINT `film_genre_ibfk_2` FOREIGN KEY (`g_id`) REFERENCES `genre` (`id_g`);

--
-- Ограничения внешнего ключа таблицы `review`
--
ALTER TABLE `review`
  ADD CONSTRAINT `review_ibfk_1` FOREIGN KEY (`film_id`) REFERENCES `film` (`id_film`) ON DELETE CASCADE,
  ADD CONSTRAINT `review_ibfk_2` FOREIGN KEY (`userexam_id`) REFERENCES `user_exam` (`id_userexam`);

--
-- Ограничения внешнего ключа таблицы `user_exam`
--
ALTER TABLE `user_exam`
  ADD CONSTRAINT `user_exam_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id_role`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
