import QtQuick 6.9
import QtQuick.Controls 6.9

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Sexbook"

    Page {
        anchors.fill: parent

        Column {
            anchors.centerIn: parent
            spacing: 10

            Text {
                text: "Welcome to Sexbook"
                font.pixelSize: 20
            }

            Button {
                text: "Click Me"
                onClicked: console.log("Button clicked!")
            }
        }
    }
}
