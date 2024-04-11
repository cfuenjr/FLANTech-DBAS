<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/cfuenjr/FLANTech-DBAS">
    <img src=https://github.com/cfuenjr/FLANTech-DBAS/assets/155736962/1805b903-7f6e-4d19-a492-3e60ae78e6c0 alt="Logo" width="140" height="140">
  </a>

<h3 align="center">Dual Biometric Authentication System</h3>

  <p align="center">
    A proof of concept security system that uses two forms of biometric authentication: fingerprint scanning and gait identification.
    <br />
    <a href="https://github.com/cfuenjr/FLANTech-DBAS"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/cfuenjr/FLANTech-DBAS">View Demo</a>
    ·
    <a href="https://github.com/cfuenjr/FLANTech-DBAS/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/cfuenjr/FLANTech-DBAS/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Current security systems, including keycard readers and keypads that are widely used on ATMs or company security, had several flaws. Traditional security systems like keycard readers and keypads are vulnerable to exploitation, risking theft of sensitive data. Current options on the market are unreliable due to poor security and the need to memorize passwords. To address this, we developed a security method that gives users security clearance by combining two forms of biometric authentication, fingerprint analysis and gait recognition. Gait is a biometric feature that is defined by how a person walks. The system needs to be secure and reliable such that users can have security clearance easily and free of any malicious attackers. Our initial design used two different inputs: a video camera and fingerprint scanner connected to a Raspberry Pi which are placed next to the device or entrance requiring access. The system uses gait recognition to identify the user’s unique method of walking. We used a post-processing Python script to eliminate the background and isolate a person walking and then we used a Convolutional Neural Network (CNN) to train our model to identify a unique feature from a person walking. We then used a matching algorithm to compare feature vectors of two individuals and determined their similarities. Along with gait recognition, our system uses a fingerprint scanner that identifies users by their unique fingerprint signatures. We utilized the Scale-Invariant Feature Transform (SIFT) algorithm to pinpoint distinct, scale and rotation-invariant features of the fingerprint known as key points. The fingerprint algorithm had 85% accuracy or higher in determining if the input has a match within the existing database. This ensured consistent results, unaffected by the image's size or orientation. The combined result of the two forms of verification of the user’s identity and would allow users access to high-security systems.




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
![03121-ezgif com-video-to-gif-converter](https://github.com/cfuenjr/FLANTech-DBAS/assets/155736962/04e49ffb-601f-4773-bea9-cb73b89b37de)
![0312-ezgif com-video-to-gif-converter](https://github.com/cfuenjr/FLANTech-DBAS/assets/155736962/f4864147-4009-4239-8e1f-86d6fa3575b5)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

* [Irfan Ali](irfan-linkedin-url) - UIC Computer Engineering Undergraduate - msiddi54@uic.edu 
* [Cesar Fuentes](linkedin-url) - UIC Computer Engineering Undergraduate - cfuen3@uic.edu
* Allan Li - UIC Computer Engineering Undergraduate - ali35@uic.edu
* [Nathan Nguyen](nate-linkedin-url) - UIC Computer Engineering Undergraduate - nnguye83@uic.edu


Project Link: [(https://github.com/cfuenjr/FLANTech-DBAS/)](https://github.com/cfuenjr/FLANTech-DBAS/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Advisor: [Dr. Lo’ay Abu Salah](advisor-url), labusa1@uic.edu
* Faculty Instructor: [Dr. Renata A Revelo](faculty-url), revelo@uic.edu
* Senior Design Lab Manager: [Anthony Flowers](manager-url), aflowe4@uic.edu
* Mohammad Abbaszada, mabbas21@uic.edu
* Furkan Basim, fbasim2@uic.edu
* Nga Vu, nvu8@uic.edu


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[advisor-url]: https://ece.uic.edu/profiles/loay-abu-salah-phd/
[faculty-url]: https://ece.uic.edu/profiles/renata-revelo-phd/
[manager-url]: https://ece.uic.edu/profiles/flowers-anthony/
[FlanTechLogo]: https://github.com/cfuenjr/FLANTech-DBAS/assets/155736962/1805b903-7f6e-4d19-a492-3e60ae78e6c0
[contributors-shield]: https://img.shields.io/github/contributors/cfuenjr/FLANTech-DBAS.svg?style=for-the-badge
[contributors-url]: https://github.com/cfuenjr/FLANTech-DBAS/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/cfuenjr/FLANTech-DBAS.svg?style=for-the-badge
[forks-url]: https://github.com/cfuenjr/FLANTech-DBAS/network/members
[stars-shield]: https://img.shields.io/github/stars/cfuenjr/FLANTech-DBAS.svg?style=for-the-badge
[stars-url]: https://github.com/cfuenjr/FLANTech-DBAS/stargazers
[issues-shield]: https://img.shields.io/github/issues/cfuenjr/FLANTech-DBAS.svg?style=for-the-badge
[issues-url]: https://github.com/cfuenjr/FLANTech-DBAS/issues](https://github.com/cfuenjr/FLANTech-DBAS/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/cfuenjr/FLANTech-DBAS.svg?style=for-the-badge
[license-url]: https://github.com/cfuenjr/FLANTech-DBAS/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/cesarfuentesjr
[nate-linkedin-url]: https://linkedin.com/in/nathan-nguyen369
[irfan-linkedin-url]: https://www.linkedin.com/in/irfan-siddiq-41ab46192/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
