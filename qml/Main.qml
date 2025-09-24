import QtQuick 6.9
import QtQuick.Controls 6.9
import QtQuick.Shapes 1.9

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "Sexbook"

    FontLoader {
        id: normal
        source: "../assets/font/balsamiq_sans_regular.ttf"
    }

    Page {
        anchors.fill: parent
        background: Rectangle {
            anchors.fill: parent
            color: "#FFFBFF"
        }

        ListView {
            anchors.fill: parent
            model: reportListModel
            spacing: 8

            delegate: Rectangle {
                width: parent.width * 0.7
                height: 60
                anchors.horizontalCenter: parent.horizontalCenter
                color: "#FFD422"
                radius: 12

                Shape {
                    id: clock
                    property real size: 36

                    x: 12
                    y: 12
                    width: size
                    height: size
                    anchors {
                        right: parent
                        top: parent
                    }

                    ShapePath {
                        fillColor: "#FFF"
                        joinStyle: ShapePath.MiterJoin

                        PathRectangle {
                            x: 0
                            y: 0
                            width: clock.size
                            height: clock.size
                            radius: clock.size / 2
                        }
                    }
                }

                TextEdit {
                    text: name
                    anchors.centerIn: parent
                    font.family: normal.font.family
                    font.weight: normal.font.weight
                    font.styleName: normal.font.styleName
                    font.pixelSize: 18
                    color: "#9A7C00"
                }
            }
        }
    }
}
