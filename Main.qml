import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: window
    width: 400
    height: 500
    visible: true
    title: qsTr("Giriş Yap")

    // Arka plan rengi (Koyu Modern Tema)
    background: Rectangle {
        color: "#1e1e24"
    }

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20
        width: parent.width * 0.8

        // Başlık Paneli
        ColumnLayout {
            Layout.alignment: Qt.AlignHCenter
            spacing: 5

            Text {
                text: "Hoş Geldiniz"
                font.pixelSize: 28
                font.bold: true
                color: "#ffffff"
                Layout.alignment: Qt.AlignHCenter
            }

            Text {
                text: "Lütfen hesabınıza giriş yapın"
                font.pixelSize: 14
                color: "#a0a0a5"
                Layout.alignment: Qt.AlignHCenter
            }
        }

        // Giriş Alanları Bloğu
        ColumnLayout {
            spacing: 15
            Layout.fillWidth: true

            // Kullanıcı Adı Alanı
            ColumnLayout {
                spacing: 5
                Layout.fillWidth: true

                Text {
                    text: "Kullanıcı Adı"
                    font.pixelSize: 12
                    font.bold: true
                    color: "#3498db"
                }

                TextField {
                    id: usernameInput
                    placeholderText: "example@email.com"
                    placeholderTextColor: "#666"
                    color: "#ffffff"
                    Layout.fillWidth: true
                    selectByMouse: true
                    font.pixelSize: 14
                    verticalAlignment: TextInput.AlignVCenter

                    background: Rectangle {
                        implicitHeight: 45
                        color: "#2a2a32"
                        border.color: usernameInput.activeFocus ? "#3498db" : "#3a3a42"
                        border.width: 1.5
                        radius: 8
                    }
                }
            }

            // Şifre Alanı
            ColumnLayout {
                spacing: 5
                Layout.fillWidth: true

                Text {
                    text: "Şifre"
                    font.pixelSize: 12
                    font.bold: true
                    color: "#3498db"
                }

                TextField {
                    id: passwordInput
                    placeholderText: "••••••••"
                    placeholderTextColor: "#666"
                    color: "#ffffff"
                    echoMode: TextInput.Password // Şifreyi gizler
                    Layout.fillWidth: true
                    selectByMouse: true
                    font.pixelSize: 14
                    verticalAlignment: TextInput.AlignVCenter

                    background: Rectangle {
                        implicitHeight: 45
                        color: "#2a2a32"
                        border.color: passwordInput.activeFocus ? "#3498db" : "#3a3a42"
                        border.width: 1.5
                        radius: 8
                    }
                }
            }
        }

        // Buton Alanı
        Button {
            id: loginButton
            text: "Giriş Yap"
            Layout.fillWidth: true
            Layout.topMargin: 10

            // Butona tıklandığında Python tarafına veri göndermek için tetikleyici
            onClicked: {
                console.log("Kullanıcı Adı:", usernameInput.text)
                console.log("Şifre:", passwordInput.text)
                // Buraya ileride Python backend bağlantısını ekleyebilirsin
            }

            contentItem: Text {
                text: loginButton.text
                font.pixelSize: 16
                font.bold: true
                color: "#ffffff"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            background: Rectangle {
                implicitHeight: 48
                // Butonun üzerine gelindiğinde renk değiştirme (Hover efekti)
                color: loginButton.down ? "#217dbb" : (loginButton.hovered ? "#2980b9" : "#3498db")
                radius: 8

                // Yumuşak renk geçişi animasyonu
                Behavior on color {
                    ColorAnimation { duration: 150 }
                }
            }
        }
    }
}