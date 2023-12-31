PHP Composer는 PHP 프로그래밍 언어를 위한 의존성 관리 도구입니다.
Composer는 PHP 프로젝트에서 필요한 외부 라이브러리, 패키지, 프레임워크 등의 종속성을 관리하고 설치해주는 역할을 합니다.
이를 통해 개발자는 손쉽게 외부 패키지를 가져와서 사용하고 프로젝트를 관리할 수 있습니다.

Composer를 사용하면 다음과 같은 이점을 얻을 수 있습니다.

종속성 관리 : Composer는 프로젝트에 필요한 패키지와 버전을 정의하고, 이를 자동을 설치해줍니다.
이를 통해 프로젝트에 필요한 패키지들을 쉽게 관리하고 업데이트할 수 있습니다.

자동 로딩 : Composer는 자동을 클래스를 로딩하는 기능을 제공합니다. 이를 통해 필요한 클래스를 수동으로 로딩하는
번거로움을 피할 수 있고, 네임스페이스를 이용한 클래스 구조를 효율적으로 관리할 수 있습니다.

오토 로딩 : Composer는 패키지의 의존성을 자동으로 해결하여 로딩합니다. 따라서 개발자는 필요한 패키지만 정의하면
되고, 이 패키지가 의존하는 다른 패키지들은 Composer가 자동으로 처리해줍니다.

패키지 관리 : Composer는 Packagist라는 온라인 저장소를 통해 수많은 패키지를 제공합니다. 개발자는 이 저장소에서
필요한 패키지를 검색하고 설치할 수 있습니다.

Composer는 프로젝트의 "composer.json" 파일에 종속성을 정의하고, "composer.lock" 파일에 패키지의 정확한 버전과
의존성 정보를 기록합니다. 이를 통해 여러 개발자가 동일한 개발 환경을 구성하고 프로젝트를 협업하면서 일관된 종속성
관리를 할 수 있습니다.

Composer는 명령줄 도구로 사용할 수 있으며, PHP 프로젝트에서 자주 사용되는 도구입니다.

composer create-project --prefer-dist laravel/laravel laravel_crud